from flask import Flask, render_template, request, redirect, url_for,
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



@app.route('/')
def index():
    return "dian"


if __name__ == '__main__':
    app.run(debug=True)