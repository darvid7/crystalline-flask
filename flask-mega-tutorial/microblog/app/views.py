"""
@author: David Lei
@since: 12/02/2017
@modified: 

"""

from app import app

# View handlers, respond to requests. @app.route()
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

