from flask import Flask
from flask import render_template
#import sys, os
#curdir = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(curdir + "/views")

import data_calls as dc
from flask import request


app = Flask(__name__)

# Homepage

@app.route('/')
def homepage():
	return render_template('homepage.html', categories=dc.get_high_categories(), 
		navbar=dc.navbar_categories())


# Topic pages

@app.route('/forum/<category>')
@app.route('/forum/<category>/<subcat1>')
@app.route('/forum/<category>/<subcat1>/<subcat2>')
@app.route('/forum/<category>/<subcat1>/<subcat2>/<subcat3>')
def topicpage(category=None, subcat1=None, subcat2=None, subcat3=None):
	if not category:
		return render_template('errorpage.html')
	path = dc.determine_path(category, subcat1, subcat2, subcat3)
	cats = dc.determine_cats(category, subcat1, subcat2, subcat3)
	topics = dc.determine_topics(category, subcat1, subcat2, subcat3)
	return render_template('topicpage.html', path=path, categories=cats, 
		topics=topics, navbar=dc.navbar_categories())

# Responses page
@app.route('/forum/topic')
def responsespage():
	# Get topic ID from request.args
	pass

# Post page
@app.route('/forum/posttopic')
def posttopicpage():
	return render_template('posttopicpage.html', path=request.args['path'],
		navbar=dc.navbar_categories())

# Submit post page
# TODO - restrict to POST
@app.route('/forum/post/submit')
def submitpost():
	pass



if __name__ == '__main__':
	app.run(debug=True)