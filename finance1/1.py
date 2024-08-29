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
    """Show portfolio of stocks"""
    data = db.execute("SELECT * FROM stocks WHERE person_id = ?", session["user_id"])
    index = 0
    while index < len(data):
        data[index]["current_price"] = lookup(data[index]["stock_symbol"])["price"]
        data[index]["total"] = data[index]["current_price"] * data[index]["amount"]
        index += 1
    name = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["username"]
    cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    return render_template("index.html", name=name, balance=cash, data=data)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("please enter stock symbol", 400)
        elif not request.form.get("shares"):
            return apology("please enter the amount of shares u wanna buy", 400)
        elif lookup(request.form.get("symbol")) == None:
            return apology("stock is not found", 400)
        elif int(request.form.get("shares")) < 1:
            return apology("please enter a valid amount", 400)
        symbol = request.form.get("symbol")
        amount = int(request.form.get("shares"))
        stock = lookup(symbol)
        total_price = amount * stock["price"]
        balance = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        if total_price > balance[0]["cash"]:
            return apology("not enough money to buy", 400)
        balance[0]["cash"] -= total_price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance[0]["cash"], session["user_id"])
        existing = db.execute("SELECT * FROM stocks WHERE person_id = ? AND stock_symbol = ?", session["user_id"], symbol)
        if len(existing) == 0:
            db.execute("INSERT INTO stocks (person_id, stock_symbol, amount) VALUES (?, ?, ?)", session["user_id"], symbol, amount)
        else:
            db.execute("UPDATE stocks SET amount = ? WHERE person_id = ? AND stock_symbol = ?", existing[0]["amount"] + amount, session["user_id"], symbol)
        date = datetime.now()
        day = int(date.strftime("%d"))
        month = int(date.strftime("%m"))
        year = int(date.strftime("%Y"))
        db.execute("INSERT INTO history (person_id, stock_symbol, amount, year, month, day, price, action, shares) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",session["user_id"], symbol, amount, year, month, day, total_price, "BUY", amount)
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        result = lookup(symbol)
        if not symbol:
            return apology("please enter a stock symbol", 400)
        elif result == None:
            return apology("stock is not found", 400)
        result["price"] = usd(result["price"])
        return render_template("quoted.html", quoted=result)
    else:
        return render_template("quote.html")


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
        elif not request.form.get("confirm-password"):
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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("please enter the stock you want to sell", 400)
        elif not request.form.get("shares"):
            return apology("please enter the amount you want to sell", 400)
        elif lookup(request.form.get("symbol")) == None:
            return apology("stock is not found", 400)
        elif int(request.form.get("shares")) < 1:
            return apology("please enter a valid amount", 400)
        symbol = request.form.get("symbol")
        amount = int(request.form.get("shares"))
        portofolio_data = db.execute("SELECT * FROM stocks WHERE person_id = ? AND stock_symbol = ?", session["user_id"], symbol)
        stock = lookup(symbol)
        if len(portofolio_data) == 0:
            return apology("you dont have the stock that you entered", 400)
        elif amount > portofolio_data[0]["amount"]:
            return apology("not enough stocks in your portofolio", 400)
        total_price = amount * stock["price"]
        balance = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        balance[0]["cash"] += total_price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance[0]["cash"], session["user_id"])
        portofolio_amount = portofolio_data[0]["amount"]
        portofolio_amount -= amount
        db.execute("UPDATE stocks SET amount = ? WHERE person_id = ? AND stock_symbol = ?", portofolio_amount, session["user_id"], symbol)
        if db.execute("SELECT * FROM stocks WHERE person_id = ? AND stock_symbol = ?", session["user_id"], symbol)[0]["amount"] == 0:
            db.execute("DELETE FROM stocks WHERE person_id = ? AND stock_symbol = ?", session["user_id"], symbol)
        date = datetime.now()
        day = int(date.strftime("%d"))
        month = int(date.strftime("%m"))
        year = int(date.strftime("%Y"))
        db.execute("INSERT INTO history (person_id, stock_symbol, amount, year, month, day, price, action, shares) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",session["user_id"], symbol, amount, year, month, day, total_price, "SELL", amount)
        return redirect("/")
    else:
        return render_template("sell.html")
