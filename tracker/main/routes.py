import os
from flask import Flask, Blueprint, render_template, redirect, url_for, flash
from tracker import app
from tracker.main.forms import PeriodForm
from tracker.model import Period
from tracker import db

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/tracker")
def tracker():
    return render_template("main/tracker.html")


@main.route("/tracker/period", ["GET", "POST"])
def period():
    form = PeriodForm()
    if form.validate_on_submit():
        period = Period(
            startdate=form.startdate.data,
            duration_days=form.duration_days.data,
            cycle_length=form.cycle_length.data,
        )
        try:
            db.session.add(period)
            db.session.commit()
            return redirect(url_for("main.period_calculator"))
        except:
            return redirect(url_for("main.period_calculator"))

    return render_template(
        "calculator/period.html", title="Period Calculator", form=form
    )


@main.route("/tracker/tools/result")
def period_calculator():
    return render_template("calculator/period.html")
