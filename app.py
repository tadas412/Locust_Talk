from flask import Flask
import "views/homepage.py"

app = Flask(__name__)

@app.route('/')
def homepage():
	return homepage_view()

if __name__ == '__main__':
	app.run(debug=True)