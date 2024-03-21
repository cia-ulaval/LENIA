from flask import Flask, render_template, url_for
from jinja2.exceptions import TemplateNotFound


app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        return 'Index pas encore créé :( '

@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        return 'About pas encore créé :( '

@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except TemplateNotFound:
        return 'Contact pas encore créé :( '

if __name__ == '__main__':
    app.run(debug=True)
