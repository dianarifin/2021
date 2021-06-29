import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'


@app.route('/')
def index():
    conn = get_db_connection()

    datas = conn.execute('SELECT id, name_company, email_company, password_company, domain_company FROM pemilik_produk').fetchall()

    conn.close()

    return render_template("index.html", data = datas)


@app.route('/<id>')
def redirect(id):
    conn = get_db_connection()

    aku = conn.execute('SELECT domain_company FROM pemilik_produk WHERE id = ?', (id,)).fetchall()

    conn.close()

    return render_template('tampil.html', data = aku)


if __name__ == '__main__':
    app.run(debug=True)
