from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this to a strong key

# Flask-Mail Configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME", "your-email@gmail.com")  # Replace with your email
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD", "your-app-password")  # Use an App Password (DO NOT use real password)
app.config["MAIL_DEFAULT_SENDER"] = app.config["MAIL_USERNAME"]

mail = Mail(app)

# Serve Portfolio Pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("project.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        if not name or not email or not phone or not message:
            flash("❌ All fields are required!", "danger")
            return redirect("/contact")

        msg = Message("New Contact Form Submission",
                      sender=app.config["MAIL_DEFAULT_SENDER"],
                      recipients=["your-email@gmail.com"])  # Replace with your email
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash("✅ Message sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error sending email: {e}", "danger")

        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
