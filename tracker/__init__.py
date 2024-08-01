import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from tracker import auth
from tracker import landing


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
db = SQLAlchemy()


app.config["SECRET_KEY"] = "9274c2804e274b709c330f4773370c88"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "project.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# initialize the app with the extension
db.init_app(app)

from tracker.auth.routes import auth as auth_blueprint
from tracker.landing.routes import landing as landing_blueprint


app.register_blueprint(auth_blueprint)
app.register_blueprint(landing_blueprint)

print("Blueprint registered successfully")
