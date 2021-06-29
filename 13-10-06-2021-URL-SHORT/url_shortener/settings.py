
# tidak bekerja 

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

SLQALCHEMY_DATABASE_URI = database_file #os.environ.get('DATABASE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False
