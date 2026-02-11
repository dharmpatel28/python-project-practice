from flask import Flask

app = Flask(__name__)

@app.route('/') # route or weblink
def hello():
    return 'hello users'

@app.route('/dharm') # link ending with '/dharm'
def dharm():
    return 'hello new users..welcome to my website.. glad to serve you services'

app.run(debug = True) #mandatory for output. 

# 'debug = True' used for detect changes and automatic make changes in output without run program