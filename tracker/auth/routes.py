from flask import Flask, Blueprint, render_template

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/")
def login():
    return render_template("users/login.html")


@auth.route("/register")
def register():
    return render_template("users/register.html")
