from flask import Flask, Blueprint, render_template

landing = Blueprint("landing", __name__, template_folder="templates")


@landing.route("/")
@landing.route("/home")
def home():
    return render_template("landing/home.html")
