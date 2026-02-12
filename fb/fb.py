import pymysql
import os
from flask import Flask, render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
from datetime import datetime
import json

conn = pymysql.connect(host='localhost',user='root',password='Dharm3059@',database='fb')

cur = conn.cursor()

# with open('config.json','r') as c:
#     params = json.load(c)["params"]

local_server= True

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mov'])

app.config['UPLOAD_FOLDER']= "E:\\py tutorial\\fb\\static\\image"

@app.route('/')
def homepage():
   
    return render_template('homepage.html')


@app.route('/post/<string:posts_slug>', methods=['GET', "POST"])
def post_route(posts_slug):

    cur.execute("SELECT * FROM posts")
    data = list(cur.fetchall())

    IMG_LIST = os.listdir('static/image')
    IMG_LIST = ['image/' + i for i in IMG_LIST]

    

    if request.method == 'POST':
        name = request.form.get('name')
        slug= request.form.get('slug')
        subject= request.form.get('subject')
        image= request.files['file1']
        date = datetime.now()

        f=request.files['file1']
        filename=secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        insert='insert into posts(name, slug, subject,date,image) values(%s, %s, %s, %s,%s)'
        values= (name, slug, subject,date,image)
        
        cur.execute(insert,values)
        conn.commit()

        return render_template('post.html', data=data)
    
    for i,j in zip(IMG_LIST,data):
        print(i)
        print(j) 
    
    return render_template('post.html', data=data,imagelist=IMG_LIST,i=i)

app.run(debug = True)