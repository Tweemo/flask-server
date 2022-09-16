'''
Flask Server
'''

from flask import Flask

app = Flask(__name__)

# Members API Routes
@app.route('/members')
def members():
    '''Returns a list of members'''
    return {
      "members": ["Member 1", "Member 2", "Member 3"]
    }

@app.route('/hello')
def hello():
    '''Returns a greeting'''
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
