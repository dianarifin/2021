from flask import Flask, render_template

app = Flask(__name__)


data_mahasiswa  = [
    {
        'nama' : 'Dian Arifin',
        'kelas' : 'aas',
        'alamat' : 'ngawi'},

    {
        'nama' : 'Dian Mala',
        'kelas' : 'asasasasa',
        'alamat' : 'Sidoarjo'}
]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data_mahasiswa")
def data_m():

    return render_template("data-mahasiswa.html", data_mahasiswa=data_mahasiswa)


@app.route("/artikel/<info>")
def artikel_info(info):
    return "halaman artikel" + info


if __name__ == "__main__":
    app.run(debug=True)