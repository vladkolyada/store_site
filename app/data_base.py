from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

from loader import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)
