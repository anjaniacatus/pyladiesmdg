from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap  import  Bootstrap



app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/activities')
def activity():
    return  render_template('ateliers.html')
@app.route('/inspiring')
def inspiring():
    return  render_template('inspiring.html')
@app.route('/template')
def template():
    return  render_template('templates.html')
nav = Nav()
nav.register_element('top', Navbar(
    View('*','home'),
    View('aboutus', 'home'),
    View('events', 'activity'),
    View('getinvolved','inspiring'),
))

nav.init_app(app)
if __name__ == '__main__':
    #app.run(debug=False, host='192.168.1.3', port=7000)
    app.run(debug=True)

