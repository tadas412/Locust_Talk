Locust Talk
========

Web app that allows visitors to post messages on a forum-style board.

Github: 
Heroku live app: locust-talk.herokuapp.com

<h2> Overview </h2>

This app uses Python's Flask library and some basic HTML to present a functional forum-style board, intended for use by Penn students. Backend data storage uses PostgreSQL. 

The simplest way to use Locust Talk is to visit the live site on locust-talk.herokuapp.com. Use the buttons to navigate to the category that interests you. Then, you can either create a new topic, or enter an existing topic by clicking the corresponding hyperlink. You can then view messages, or post a new response by clicking the button at the buttom of the page. 

<h2> Features </h2>

<ul>
	<li> Navigate through a hierarchy of categories </li>
	<li> View both category topics and subcategory links on each page </li>
	<li> Create new topics </li>
	<li> View message streams for each topic </li>
	<li> Add messages (responses) to topics </li>
	<li> View messages in pages of 5 max, with the ability to go to other pages </li>
</ul>

<h2> CIS 192 Final Project Requirements </h2>

<h3> Your app should be callable from the command line, and should take as input at least two arguments/flags that determine its usage, which you should consume using the optparse module. </h3>

Locust Talk is callable from the command line on a local machine with the usage "python app.py [-d] [-p PORT]". The -d argument should be True or False based on if you want Flask to run in debugging mode - the application will be allowed to execute arbitrary Python code on your computer. If you're in debugging mode, the app will also print out a log of the functions it's using and associated times (in seconds) that they start. The -p PORT argument determines on which port to mount the app when it runs locally.


<h3> Define and use a custom class (okay to inherit from something else, as in wxpython). </h3>

There are two custom classes defined in data/data_classes.py. 

The first one is Topic, which stores information about a particular conversation topic (topic name, topic ID, author, category, subcategories), and also has a couple methods for managing messages related to a topic (get_messages and add_message). The method get_num_pages checks how many messages are associated with the topic and returns the number of pages needed to hold them.

The other one is Message, which simply stores information about a particular message (message ID, message, author).

<h3> Define at least one magic method. </h3>

Each of the custom classes described above have init, repr, and eq methods. 

<h3> Use at least two of the following modules: itertools, random, re, os </h3>

In app.py, I used <b>os</b> to add the relative path /data to the system path. In particular, os was used to grab the current directory name, and then /data was appended to that path, which was added to the system path. This allowed me to store python modules in /data. 

Also in app.py, I used <b>itertools</b> to islice messages onto the correct pages corresponding to a topic. If there are more than 5 messages, islice selects the five (or fewer) that should be present on the current page.

<h3> Define and use a custom decorator. </h3>

My custom decorator is defined in /data/utils.py. It is a debugger decorator, with which I decorated all non-routing functions. If the -d flag is used when running the app, this will result in those decorated functions printing when they are called: their name, args, and time passed since start is printed. 


<h3> Include documentation with a detailed explanation of how to use your app. Be sure to point out anything especially cool that you did! </h3>

This document explains usage of the app. The most relevant features to note:

<ul>
Use of PostgreSQL usage to persistently store all data
Full integration and functionality with live Heroku app
Fully up and running on Heroku
Page counter / slicer is pretty cool
</ul>


<h2> Design Process </h2>

<h2> Database Structure </h2>


topics
<t>	topic_id <br>
<t>	topic_name <br>
<t>	author <br>
<t>	category <br>
<t>	subcat1 <br>
<t>	subcat2 <br>
<t>	subcat3 <br>


messages
<t>	message_id <br>
<t>	author <br>
<t>	message <br>
<t>	topic_id (foreign key dependent) <br>


All varchar(32), varchar(128), or bigint

<h2> Next Steps </h2>

I hope to continue this project over winter break - the next step is to integrate Bootstrap into it, so that it actually looks nice and is usable. Beyond that, some basic admin functions (e.g. delete responses or topics) would be useful, along with various features like displaying a preview of the latest post associated with a topic, the number of posts associated with a topic, having a widget on the homepage that points out hot topics, etc.


<h2> References </h2>

https://devcenter.heroku.com/articles/getting-started-with-python-o - Setting up Flask to work with Heroku

Python Docs

Postgresql Docs
