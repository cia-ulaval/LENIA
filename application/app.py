from flask import Flask, render_template, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/about')
def about():
    return 'About Us'

@app.route('/contact')
def contact():
    return 'Contact Page'

if __name__ == '__main__':
    app.run(debug=True)
