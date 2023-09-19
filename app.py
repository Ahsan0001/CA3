from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/subtract/<first>/<second>', methods=['GET'])
def subtract_route(first, second):  # put application's code here
    return int(first) - int(second)

if __name__ == '__main__':
    app.run()
