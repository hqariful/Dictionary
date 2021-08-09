from flask_wtf import FlaskForm
from wtforms import StringField

class Register(FlaskForm):
    word = StringField("Word")
    meaning = StringField("Meaning")