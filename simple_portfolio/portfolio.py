from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime


app =Flask(__name__)


# for gmail notification
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME= 'dharm3059@gmail.com',
    MAIL_PASSWORD = 'Dharm3059@'
)
mail =Mail(app)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:Dharm3059@@localhost/portfolio'
db= SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    subject= db.Column(db.String(80),nullable=False)
    message= db.Column(db.String(80),nullable=False)
    date = db.Column(db.String(80),nullable=False)


@app.route('/', methods=['GET', 'POST'])
def page():
    return render_template('index.html')

@app.route('/mail', methods=['POST'])
def sendmail():
    if request.method=='POST':
        "add entry to database"
        name1 = request.form.get('name')
        print(name1)
        email1 = request.form.get('email')
        subject1 = request.form.get('subject')
        message1 = request.form.get('message')

        

        entry = Contacts(name=name1, email=email1,subject=subject1,message=message1,date=datetime.now()) 
        db.session.add(entry)
        db.session.commit()

        mail.send_message('New message from '+ name1, 
                        sender = email1, 
                        recipients = 'dharm3059@gmail.com', 
                        body = message1
                        )

app.run(debug = True)