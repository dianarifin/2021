from flask import Flask, render_template, request, url_for

app = Flask(__name__)


class company():

    @app.route("/index")
    @app.route("/")
    def index():

        return render_template("index.html")

    @app.route("/daftar", methods=["POST", "GET"])
    def daftar():

        return render_template("daftar.html")

    @app.route("/login", methods=["POST", "GET"])
    def login():

        return render_template("login.html")


# class member():





















if __name__ == "__main__":
    app.run(debug=True)