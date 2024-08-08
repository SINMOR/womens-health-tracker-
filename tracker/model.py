from datetime import datetime
from tracker import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    periods = db.relationship(
        "Period", backref="user", lazy=True
    )  # inputs a  one to many relationship with the period table
    ovulation = db.relationship(
        "Ovulation", backref="user", lazy=True
    )  # inputs a  one to many relationship with the period table

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.date_of_birth}')"


class Period(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
    )  # declare user.id as the foreign key
    start_date = db.Column(db.Date, nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)
    cycle_length = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"Period('{self.start_date}','{self.duration_days}','{self.cycle_length}')"
        )


class Ovulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
    )  # declare user.id as the foreign key
    start_date = db.Column(db.Date, nullable=False)
    cycle_length = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Ovulation('{self.start_date}','{self.cycle_length}','{self.cycle_length}')"
