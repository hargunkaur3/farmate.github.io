# -*- coding: utf-8 -*-
"""basic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ESac7lusG-yrMbiRqtDreBeEV4WkGC9m
"""

from flask import Flask, render_template
pip install flask


app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('services.html')


if __name__ == "__main__":
    app.run(debug=True)
