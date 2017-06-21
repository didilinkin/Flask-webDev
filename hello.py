from flask import flask
app = Flask(__name__)

@app.router('/')
def index():
    return '<h1> Hello World! </h1>'

@app.router('/user/<name>')

def use(name):
    return '<h1> Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)