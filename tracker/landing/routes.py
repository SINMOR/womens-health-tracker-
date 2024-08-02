import os
from flask import Flask, Blueprint, render_template, send_from_directory
from tracker import app

landing = Blueprint("landing", __name__, template_folder="templates")


@landing.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@landing.route("/")
@landing.route("/home")
def home():
    return render_template("landing/home.html", title="Home")
