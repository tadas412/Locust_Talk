from flask import Flask
from flask import render_template
from flask import redirect
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

@app.route('/forum/view/<category>')
@app.route('/forum/view/<category>/<subcat1>')
@app.route('/forum/view/<category>/<subcat1>/<subcat2>')
@app.route('/forum/view/<category>/<subcat1>/<subcat2>/<subcat3>')
def topicpage(category=None, subcat1=None, subcat2=None, subcat3=None):
	if not category:
		return render_template('errorpage.html')
	path = dc.determine_path(category, subcat1, subcat2, subcat3)
	cats = dc.determine_cats(category, subcat1, subcat2, subcat3)
	topics = dc.determine_topics(category, subcat1, subcat2, subcat3)
	return render_template('topicpage.html', path=path, categories=cats, 
		topics=topics, navbar=dc.navbar_categories())

# Responses page
@app.route('/forum/view')
def responsespage():
	topic_id = int(request.args['topic_id'])
	topic = dc.get_topic_by_id(topic_id)
	messages = dc.get_messages(topic_id)
	return render_template('messagepage.html', topic_name=topic.topic_name, 
		messages=messages, navbar=dc.navbar_categories(), topic_id=topic_id)



# Post topic page
@app.route('/forum/posttopic')
def posttopicpage():
	return render_template('posttopicpage.html', path=request.args['path'],
		navbar=dc.navbar_categories())

# Submit post page
# TODO - restrict to POST
@app.route('/forum/posttopic/submit', methods=['POST'])
def submitposttopic():
	print request.form
	dc.add_topic(request.form['name'], request.form['topic_title'], 
		request.form['path'])
	return redirect('/forum/view/{0}'.format(request.form['path']))



# Post message page
@app.route('/forum/postmessage')
def postmessagepage():
	topic_id = int(request.args['topic_id'])
	topic = dc.get_topic_by_id(topic_id)
	return render_template('postmessagepage.html', topic=topic,
		navbar=dc.navbar_categories())

# Submit post message
@app.route('/forum/postmessage/submit', methods=['POST'])
def submitpostmessage():
	topic_id = int(request.form['topic_id'])
	dc.add_message(topic_id, request.form['name'], request.form['message'])
	return redirect('/forum/view?topic_id={0}'.format(topic_id))



if __name__ == '__main__':
	app.run(debug=True)