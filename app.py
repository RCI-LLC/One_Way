from flask import Flask, request, redirect, send_from_directory
import os
import smtplib
from email.message import EmailMessage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

# ---------- Email configuration (set these as environment variables) ----------
# GMAIL_ADDRESS   = the Gmail account that will SEND the message (e.g. yourshop@gmail.com)
# GMAIL_APP_PASSWORD = a 16-character Gmail "App Password" (NOT your normal Gmail password)
# CONTACT_RECIPIENT = the inbox that should RECEIVE messages (admin@oneway.com)
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
CONTACT_RECIPIENT = os.environ.get("CONTACT_RECIPIENT", "admin@oneway.com")


# ---------- Page routes (serve the plain HTML files directly) ----------
@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/about.html")
def about():
    return send_from_directory(BASE_DIR, "about.html")


@app.route("/photos.html")
def photos():
    return send_from_directory(BASE_DIR, "photos.html")


@app.route("/contact.html")
def contact():
    return send_from_directory(BASE_DIR, "contact.html")


@app.route("/contracts.html")
def contracts():
    return send_from_directory(BASE_DIR, "contracts.html")


# ---------- Static assets (CSS, images, etc.) ----------
@app.route("/style.css")
def style():
    return send_from_directory(BASE_DIR, "style.css")


@app.route("/<path:filename>")
def any_file(filename):
    # Lets image files (e.g. photo1.jpg) dropped in this folder be served too.
    return send_from_directory(BASE_DIR, filename)


# ---------- Contact form handling ----------
def send_contact_email(name, email, message):
    """Send the contact form submission to CONTACT_RECIPIENT via Gmail SMTP."""
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        # Credentials aren't configured yet -- fall back to logging so the
        # site doesn't crash, but this means email is NOT actually sending.
        print("WARNING: GMAIL_ADDRESS / GMAIL_APP_PASSWORD not set. Email not sent.")
        print(f"New contact message:\nName: {name}\nEmail: {email}\nMessage: {message}\n")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"New contact form message from {name}"
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = CONTACT_RECIPIENT
    msg["Reply-To"] = email  # so replying goes straight to the customer
    msg.set_content(
        f"New message from the One-Way ATV Powersports contact form:\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n\n"
        f"Message:\n{message}\n"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)
    return True


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return redirect("/contact.html?status=error")

    try:
        send_contact_email(name, email, message)
    except Exception as e:
        print(f"Failed to send contact email: {e}")
        return redirect("/contact.html?status=error")

    return redirect("/contact.html?status=success")


if __name__ == "__main__":
    app.run(debug=True)
