import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

db = SQL("sqlite:///finance.db")


data = db.execute("SELECT * FROM stocks WHERE person_id = ?", 1)
index = 0
while index < len(data):
    data[index]["current_price"] = 100
    data[index]["total"] = data[index]["current_price"] * data[index]["amount"]
    index += 1

print(data)