from flask_classful import FlaskView
from flask import render_template

class TestClass(FlaskView):

    def index(self):
        return "<h1>This is my index page</h1>"

    def welcome(self): #/welcome
        return "<h1>This is my Welcome page</h1>"

    def ariwelcome(self):
        return render_template('index_op.html')