"""
@author: David Lei
@since: 28/11/2016
@modified: 

"""
from flask import Flask
app = Flask(__name__)

# function mapped to route /
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about/')
def about():
    return 'Life is one\'s journey through life'

if __name__ == '__main__':
    app.run(debug=True)         # allows to print out errors, in production set to false because of security
    # localhost:5000
    # python3 Hello-World.py
