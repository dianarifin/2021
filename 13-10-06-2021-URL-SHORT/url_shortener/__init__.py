import os
from flask import Flask 

from .extensions import db
from .routes import short


def create_app():
    
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

    app.config['SECRET_KEY'] = 'masmbakinirahasiayasecret!'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_file # os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config.from_pyfile(config_file)

    db.init_app(app)
    
    app.register_blueprint(short)

    return app

if __name__ == '__main__':
    app.run(debug=True)