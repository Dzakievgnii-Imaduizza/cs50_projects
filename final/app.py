import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    menfess_data = db.execute("SELECT * FROM menfess order by menfess_id desc")
    return render_template("index.html", database=menfess_data)

@app.route("/history")
@login_required
def history():
    personal_menfess = db.execute("SELECT * FROM menfess WHERE sender_id = ? order by menfess_id desc", session["user_id"])
    return render_template("my_menfess.html", database=personal_menfess)


@app.route("/post", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        if not request.form.get("sender"):
            return apology("please enter a name or an anonym", 400)
        elif not request.form.get("mention"):
            return apology("please enter someone to mention", 400)
        elif not request.form.get("message"):
            return apology("please enter a message", 400)
        sender = request.form.get("sender")
        mention = request.form.get("mention")
        message = request.form.get("message")
        date = datetime.now()
        formated_time = date.strftime("%d/%m/%Y")
        db.execute("INSERT INTO menfess (message, time, sender, mention, sender_id) VALUES (?, ?, ?, ?, ?)", message, formated_time, sender, mention, session["user_id"])
        return redirect("/")
    else:
        return render_template("post.html")

@app.route("/delete", methods=["POST"])
@login_required
def delete():
    id = request.form.get("id")
    db.execute("DELETE FROM menfess WHERE menfess_id = ?", id)
    return redirect("/history")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # clear session
    session.clear()

    # if request method is post
    if request.method == "POST":
        # check errors
        same_username = db.execute("SELECT username FROM users WHERE username = ?", request.form.get("username"))
        if not request.form.get("username"):
            return apology("must provide username", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("unconfirmed password", 400)
        elif len(same_username) > 0:
            return apology("username has been taken, try a different username", 400)

        # set user inputs as username and password
        username = request.form.get("username")
        # password = request.form.get("password")
        hashed_password = generate_password_hash(request.form.get("password"))

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed_password)

        user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = user_id[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")
