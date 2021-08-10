from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class Register(FlaskForm):
    word = StringField("Word")
    meaning = TextAreaField("Meaning",render_kw={"rows": 10, "cols": 20})

