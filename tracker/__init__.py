from flask import Flask, Blueprint
from tracker  import auth

app = Flask(__name__)


from tracker.auth.routes import auth as auth_blueprint

# from tracker.landing.routes import landing as landing_blueprint


app.register_blueprint(auth_blueprint)
# app.register_blueprint(landing_blueprint)
