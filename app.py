from flask import Flask, render_template, request
from classTest.TestClass import TestClass
from classTest.Home import HomeIndex

app = Flask(__name__)
host= '0.0.0.0'
port = '8080'

TestClass.register(app,route_base = '/app/')

@app.route("/")
def hello_world():
    return render_template('index_op.html')

@app.route("/login", methods=['POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@app.route("/loginTest", methods=['POST'])
def loginTest():
    return {
        "result":"ok"
    }

if __name__=='__main__':
    app.run(debug=True, host=host, port = port)