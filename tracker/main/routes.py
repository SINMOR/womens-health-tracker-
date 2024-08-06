import os
from flask import Flask, Blueprint, render_template
from tracker import app

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/tracker")
def tracker():
    return render_template("main/tracker.html")
