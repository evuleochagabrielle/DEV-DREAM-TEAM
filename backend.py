from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import hashlib
import datetime
import pytz

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"

@app.route("/")
def index():
    return redirect(url_for("register"))

@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").strip().lower()
        password = request.form.get("password")

        # TO DO: implement user creation logic without FaunaDB
        # For example, you could use a local database or a different cloud database
        # For demonstration purposes, I'll just store the user in a dictionary
        users = {}  # replace with your database or storage mechanism
        if username in users:
            flash("The account you are trying to create already exists!", "danger")
        else:
            users[username] = {
                "password": hashlib.sha512(password.encode()).hexdigest(),
                "date": datetime.datetime.now(pytz.UTC)
            }
            flash("You have successfully created your account, you can now create online elections!", "success")
            return redirect(url_for("register"))

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)