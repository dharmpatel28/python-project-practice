from flask import Flask , render_template

app = Flask(__name__)

#page 1
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/page1')
def page1():
    name = 'dharm h patel'
    return render_template('page1.html', name2 = name)



app.run(debug=True)
