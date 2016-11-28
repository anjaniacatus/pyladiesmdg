from flask import Flask, render_template
from flask_navigation import Navigation
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

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('QuiSommesNous?', 'home'),
    nav.Item('Ateliers','activity'),
    nav.Item('Articles','inspiring'),
    ])


if __name__ == '__main__':
    app.run(debug=True)
