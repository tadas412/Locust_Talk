from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

import itertools
import time
from optparse import OptionParser

# /// Allow for imports from /data folder \\\
import sys
import os
curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curdir + "/data")  # allows import of files in /data
# /////////// End import overhead \\\\\\\\\\\

import data_calls as dc
from data_classes import Topic, Message
import utils

# Get the app started
app = Flask(__name__)


# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html',
                           categories=dc.get_high_categories(),
                           navbar=dc.navbar_categories())


# Topic pages
@app.route('/forum/view/<category>')
@app.route('/forum/view/<category>/<subcat1>')
@app.route('/forum/view/<category>/<subcat1>/<subcat2>')
@app.route('/forum/view/<category>/<subcat1>/<subcat2>/<subcat3>')
def topicpage(category=None, subcat1=None, subcat2=None, subcat3=None):
    if category == "Home":
        return redirect("/")
    elif category == "About Us":
        return redirect("/about_us")
    path = dc.determine_path(category, subcat1, subcat2, subcat3)
    if not path:
        print "WARNING: topicpage failed rendering"
        return render_template('errorpage.html')
    cats = dc.determine_cats(category, subcat1, subcat2, subcat3)
    topics = dc.determine_topics(category, subcat1, subcat2, subcat3)
    return render_template('topicpage.html', path=path, categories=cats,
                           topics=topics, navbar=dc.navbar_categories())


# About Us page
@app.route('/about_us')
def aboutus():
    return render_template('aboutus.html', navbar=dc.navbar_categories())


# Responses/messages page
@app.route('/forum/view')
def responsespage():
    try:
        topic_id = int(request.args['topic_id'])
    except (ValueError, KeyError):
        print "WARNING: responsespage could not get topic_id"
        return render_template('errorpage.html')
    topic = dc.get_topic_by_id(topic_id)
    try:
        page = int(request.args['page'])
    except KeyError:
        page = 1
    path = dc.determine_path(topic.category, topic.subcat1,
                             topic.subcat2, topic.subcat3)
    pages = [i + 1 for i in range(topic.get_num_pages())]
    # list of valid pages

    if len(pages) == 0:
        pages.append(1)
    page = page if page < max(pages) else max(pages)
    # if we're past valid, take max
    messages = topic.get_messages()
    # slice the right messages for the given page
    messages = itertools.islice(messages, (page - 1) * 5, page * 5)
    return render_template('messagepage.html', topic_name=topic.topic_name,
                           messages=messages, navbar=dc.navbar_categories(),
                           topic_id=topic_id, pages=pages, path=path)


# Post topic page
@app.route('/forum/posttopic')
def posttopicpage():
    return render_template('posttopicpage.html', path=request.args['path'],
                           navbar=dc.navbar_categories())


# Submit post page
@app.route('/forum/posttopic/submit', methods=['POST'])
def submitposttopic():
    try:
        dc.add_topic(request.form['name'], request.form['topic_title'],
                     request.form['path'])
    except KeyError:
        print "WARNING: submitposttopic key error"
        return render_template('errorpage.html')
    return redirect('/forum/view/{0}'.format(request.form['path']))


# Post message page
@app.route('/forum/postmessage')
def postmessagepage():
    try:
        topic_id = int(request.args['topic_id'])
    except (ValueError, KeyError):
        print "WARNING: postmessagepage unable to get topic_id"
        return render_template('errorpage.html')
    topic = dc.get_topic_by_id(topic_id)
    path = request.args['path']
    return render_template('postmessagepage.html', topic=topic,
                           navbar=dc.navbar_categories(), path=path)


# Submit post message
@app.route('/forum/postmessage/submit', methods=['POST'])
def submitpostmessage():
    try:
        topic_id = int(request.form['topic_id'])
    except (ValueError, KeyError):
        print "WARNING: submitpostmessage unable to get topic_id"
        return render_template('errorpage.html')
    topic = dc.get_topic_by_id(topic_id)
    topic.add_message(request.form['name'], request.form['message'])
    return redirect('/forum/view?topic_id={0}'.format(topic_id))


@utils.debug
def main():
    optparser = OptionParser()
    optparser.add_option('-p', dest="port", type="int", default="5000")
    optparser.add_option('-d', dest="debug", action="store_true",
                         default=False)
    options, _ = optparser.parse_args()
    utils.set_debug(options.debug)
    app.run(debug=utils.do_debug, port=options.port)


if __name__ == '__main__':
    main()
