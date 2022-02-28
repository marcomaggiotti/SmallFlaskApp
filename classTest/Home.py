from flask import render_template
from flask_classful import FlaskView

class HomeIndex(FlaskView):

    def welcome(self):
        return render_template('index_op.html')
