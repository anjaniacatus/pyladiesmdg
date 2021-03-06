from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap  import  Bootstrap



app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inspiring')
def joinus():
    return  render_template('helping.html')

def events():
    return  render_template('helping.html')


@app.route('/template')
def template():
    return  render_template('templates.html')
nav = Nav()
nav.register_element('top', Navbar(
    View("Pyladies Antananarivo", 'home'),
    View("About",'home'),
    View("Pourquoi?",'joinus'),
    View("Activités",'joinus'),
    View("Partenaires",'joinus'),
))

nav.init_app(app)
if __name__ == '__main__':
    #app.run(debug=False, host='192.168.1.3', port=7000)
    app.run(debug=False)

