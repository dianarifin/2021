from flask import Blueprint, render_template

from .extensions import db
from .models import Link

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    pass

@short.route('/')
def index():
    return render_template('index.html')

@short.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html', 
                            new_link=short_url, original_url=link.original_url)

@short.route('/stats')
def stats():
    pass

@short.errorhandler(404)
def page_not_found(e):
    return '', 404


