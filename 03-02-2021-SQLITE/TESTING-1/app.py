from flask import Flask, render_template, request, redirect, url_for
import database
import string, sqlite3


app = Flask(__name__)

@app.route('/register', methods=["GET", "POST"] )
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        

        database.register(username, password, email)

    return render_template("register.html")
    # return redirect("https://dianisa.com")

@app.route('/tampil')
def tampil():
    database.tampil()

    return render_template("tampil.html", tables = database.data )


@app.route('/data/<nama>')
def redirect(nama):

    # conn = sqlite3.connect('register.db')
    # c = conn.cursor()
    # cari = c.execute("SELECT email FROM register WHERE username = (?)", (nama,))

    redirect_url = 'http://localhost:5000'
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()
        # select_row = "SELECT email FROM register WHERE username = (?)", (nama)
        result_cursor = cursor.execute("SELECT email FROM register WHERE username = (?)", (nama,))
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print(e.args)
    return redirect(redirect_url)
    # return render_template("ada.html", ada = str(ubah_s) )


if '__name__' == __name__:
    app.run(debug=True)






