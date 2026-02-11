from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:Dharm3059@@localhost/portfolio'
db= SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String,unique=False,nullable=False)
    email = db.Column(db.String)
    subject= db.Column(db.String)
    message= db.Column(db.String)
    date = db.Column(db.String)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        "add entry to database"
        name1 = request.form.get('name')
        email1 = request.form.get('email')
        subject1 = request.form.get('subject')
        message1 = request.form.get('message')

        entry = Contacts(name=name1, email=email1,subject=subject1,message=message1,date=datetime.now()) 
        db.session.add(entry)
        

    return render_template('index.html')

app.run(debug =True)