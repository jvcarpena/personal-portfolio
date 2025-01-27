import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
import smtplib

# load .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")


MAIL_ADDRESS = os.getenv("EMAIL_KEY")
MAIL_APP_PW = os.getenv("PASSWORD_KEY")


def send_email(name, email, message):
    email_message = f"Subject:New Message from Portfolio\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MAIL_ADDRESS, password=MAIL_APP_PW)
        connection.sendmail(from_addr=MAIL_ADDRESS, to_addrs=MAIL_ADDRESS, msg=email_message)


@app.route("/")
def home():
    msg_sent = request.args.get("msg_sent", default=False, type=bool)  # Get the msg_sent from the query string
    return render_template("index.html", msg_sent=msg_sent)  # Pass msg_sent to the template


@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.form
    send_email(data['name'], data['email'], data['message'])
    success = True  # Assuming the message was sent successfully
    if success:
        return redirect(url_for("home", msg_sent=True) + "#contact")  # Redirect with msg_sent=True
    else:
        return redirect(url_for("home", msg_sent=False) + "#contact")  # Redirect with msg_sent=False


if __name__ == "__main__":
    app.run(debug=False)
