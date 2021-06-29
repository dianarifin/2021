from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        'author' : 'Dian Arifin',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'April 20, 2019'
    },
    {
        'author' : 'AKu Arifin',
        'title' : 'blog post 2',
        'content' : '2 post content',
        'date_posted' : 'April 20, 2019'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

