from tracker import db
from flask import Flask, Blueprint, render_template,flash,url_for,redirect
from werkzeug.security import generate_password_hash, check_password_hash
from tracker.auth.forms import RegistrationForm
from tracker.model import User 

auth = Blueprint("auth", __name__, template_folder="templates")



@auth.route("/")
def login():
    return render_template("users/login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except:
            flash('Username already exists!', 'danger')
            return redirect(url_for('auth.register'))
    return render_template("users/register.html", form=form)
