from flask import Flask, render_template, request, flash
from forms import GraphChoice
import subprocess
import requests
import time
import os
base = os.getcwd()
script = os.path.join(base,'templates')
print script

app = Flask(__name__)
app.secret_key='development'

#def index():
 #   return render_template('index.html')

# @app.route('/', methods=['GET','POST'])
#@app.route('/')
@app.route('/')
def index():
    form = GraphChoice()
    return render_template('index.html')

# @app.route('/subisu', methods=['GET', 'POST'])
# def get_graph():
#     form = GraphChoice()
#     if request.method == 'POST':
#         subisu_graph()
#         return render_template('subisu-grapher.html')
#     elif request.method == 'GET':
#         return render_template('subisu-grapher.html')
#         # return render_template('frames.html')



@app.route('/subisu')
def subisu_graph():
    # interval =  int(request.form.getlist('Interval')[0]) - 1
    # generate = GraphSubisu()
    return render_template('subisu_graph.html')

@app.route('/wlink')
def wlink_graph():
        # genrate = GraphWlink()
        return render_template('wlink_graph.html')

@app.route('/cactigraph')
def cacti_graph():
    # generate = GraphCacti()
    return render_template('cacti_graph.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8090)
