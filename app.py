from flask import Flask
from flask import render_template
import sys, os
curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curdir + "/views")
import homepage as hp

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html', l=hp.get_categories())

if __name__ == '__main__':
	app.run(debug=True)