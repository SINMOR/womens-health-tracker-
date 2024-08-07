from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
    PasswordField,
    BooleanField,
    IntegerField,
    DateField,
)
from wtforms.validators import DataRequired, ValidationError



class PeriodForm(FlaskForm):
    startdate = DateField(
        "When did your last period start?", validators=[DataRequired()]
    )
    duration_days = IntegerField(
        "How many days did it last?", validators=[DataRequired()]
    )
    cycle_length = IntegerField("Average cycle length", validators=[DataRequired()])
    submit = SubmitField("See results")


class OvulationForm(FlaskForm):
    startdate = DateField(
        "When did your last period start?", validators=[DataRequired()]
    )
    cycle_length = IntegerField("Average cycle length", validators=[DataRequired()])
    submit = SubmitField("See results")
