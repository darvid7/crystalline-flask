"""
@author: David Lei
@since: 28/11/2016
@modified: 

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    # return render_template('html_file_name.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/trigger/')
def trigger():
    return render_template('event-trigger.html')


if __name__ == "__main__":
    app.run(debug=True)