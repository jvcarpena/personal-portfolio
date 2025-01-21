import os
from dotenv import load_dotenv
from flask import Flask, abort, render_template, redirect, url_for, flash, request
import smtplib

# load .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
