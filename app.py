from flask import Flask, request, redirect, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

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


# ---------- Static assets (CSS, images, etc.) ----------

@app.route("/style.css")
def style():
    return send_from_directory(BASE_DIR, "style.css")


@app.route("/<path:filename>")
def any_file(filename):
    # Lets image files (e.g. photo1.jpg) dropped in this folder be served too.
    return send_from_directory(BASE_DIR, filename)


# ---------- Contact form handling ----------

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return redirect("/contact.html?status=error")

    # For now we just log the message to the console.
    # Later you could save it to a file, database, or send an email.
    print(f"New contact message:\nName: {name}\nEmail: {email}\nMessage: {message}\n")

    return redirect("/contact.html?status=success")


if __name__ == "__main__":
    app.run(debug=True)
