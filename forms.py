from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class Register(FlaskForm):
    word = StringField("Word")
    meaning = StringField("Meaning")

