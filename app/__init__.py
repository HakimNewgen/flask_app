from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admins.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import views
from app import admin_views
from app import registration_form
