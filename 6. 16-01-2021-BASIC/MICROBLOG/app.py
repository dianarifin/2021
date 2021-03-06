import datetime
from flask import Flask, render_template, request
import database


app = Flask(__name__)
# entries = []

database.create_tables()


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method ==  "POST":
        entry_content = request.form.get("content")
        database.create_entry(entry_content, datetime.datetime.today().strftime("%b %d"))

    return render_template("home.html", entries=database.retrieve_entries())









