from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for
from forms import Register

app = Flask(__name__)
app.config['SECRET_KEY'] = "IT'S SECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dictionary.db'

db = SQLAlchemy(app)

class WordList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30),nullable=False)
    meaning = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"(word: {self.word}, meaning: {self.meaning})"

db.create_all()

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/list')
def list():
    wordlist = WordList.query.all()
    return render_template("list.html",words = wordlist)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = Register()
    if form.validate_on_submit():
        new = WordList(word=form.word.data,meaning=form.meaning.data)
        db.session.add(new)
        db.session.commit()
        return "success"
    return render_template("register.html", form = form)

if __name__ == "__main__":
    app.run()