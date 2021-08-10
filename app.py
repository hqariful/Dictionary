from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request
from flask import request
from werkzeug.utils import redirect
from forms import Register

app = Flask(__name__)
app.config['SECRET_KEY'] = "IT'S SECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dictionary.db'

db = SQLAlchemy(app)

class WordList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30),nullable=False)
    meaning = db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"(word: {self.word}, meaning: {self.meaning}, date_posted: {self.date_posted})"

db.create_all()

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/list')
def list():
    wordlist = WordList.query.all()
    return render_template("list.html",words = wordlist)

@app.route('/delete',methods = ["GET"])
def delete():
    red = request.args.get('target')
    print(red)
    u = WordList.query.get(int(red))
    db.session.delete(u)
    db.session.commit()
    return redirect(url_for('list'))

@app.route("/edit",methods=["GET","POST"])
def edit():
    if request.method == "GET":
        form = Register()
        print('GET')
        w = WordList.query.get(int(request.args.get('id')))
        return render_template("register.html", form = form, action = "edit", word = w)
    elif request.method == "POST":
        print('POST')
        old = WordList.query.get(int(request.form['n']))
        old.word = request.form['word']
        old.meaning = request.form['meaning']
        db.session.commit()
        return redirect(url_for('list'))
    

@app.route('/register', methods = ['POST','GET'])
def register():
    form = Register()
    if form.validate_on_submit():
        new = WordList(word=form.word.data,meaning=form.meaning.data)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template("register.html", form = form, action = "register")

if __name__ == "__main__":
    app.run(debug=True)