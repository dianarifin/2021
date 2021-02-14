from flask import Flask, render_template, request


app = Flask(__name__)
entries = []

# @app.route("/home", methods=["POST","GET"])
# def home():
#     if request.method == "POST":
#         content = request.form.get("content")
#         entries.append(content)

#     return render_template("home.html", entries=entries)


class testing():
    # entries = []

    @app.route("/coba", methods=["POST","GET"])
    def home():
        if request.method == "POST":
            content = request.form.get("content")
            entries.append(content)

        return render_template("home.html", entries=entries)
