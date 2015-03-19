Locust Talk
========

MADE CHANGES

Web app that allows visitors to post messages on a forum-style board.

VIEW THIS README ON GITHUB!

Github: https://github.com/tadas412/Locust_Talk <br>
Heroku live app: locust-talk.herokuapp.com

<h2> Overview </h2>

This app uses Python's Flask library and some basic HTML to present a functional forum-style board, intended for use by Penn students. Backend data storage uses PostgreSQL. 

The simplest way to use Locust Talk is to visit the live site on locust-talk.herokuapp.com. Use the buttons to navigate to the category that interests you. Then, you can either create a new topic, or enter an existing topic by clicking the corresponding hyperlink. You can then view messages, or post a new response by clicking the button at the buttom of the page. 

Alternatively, see instructions below under "CIS 192 Final Project Requirements" for how to run the app locally.

<h2> Required Dependencies </h2>

(from requirements.txt virtual environment) <br> <br>

Flask==0.10.1 <br>
Jinja2==2.7.3 <br>
MarkupSafe==0.23 <br>
Werkzeug==0.9.6 <br>
gunicorn==19.1.1 <br>
itsdangerous==0.24 <br>
psycopg2==2.5.4 <br>
wsgiref==0.1.2 <br>

<h2> File Structure </h2>

Locust_Talk <br>
&nbsp;&nbsp;venv/ - includes all files for the virtual environment I used <br>
&nbsp;&nbsp;data/ <br>
&nbsp;&nbsp;&nbsp;&nbsp;data_calls.py - most data management done here <br>
&nbsp;&nbsp;&nbsp;&nbsp;data_classes.py - custom classes, and some corresponding data pulling methods, can be found here <br>
&nbsp;&nbsp;&nbsp;&nbsp;utils.py - misc. utilities (e.g. custom decorator for debugging) <br>
&nbsp;&nbsp;static/ - includes media files for front end, and CSS <br>
&nbsp;&nbsp;templates/ - HTML templates for the app <br>
&nbsp;&nbsp;app.py - main orchestrator and router for the app <br>
&nbsp;&nbsp;Procfile - file that tells Heroku what to run <br>
&nbsp;&nbsp;requirements.txt - file that tells Heroku what dependencies we have <br>


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

<h4> Your app should be callable from the command line, and should take as input at least two arguments/flags that determine its usage, which you should consume using the optparse module. </h4>

Locust Talk is callable from the command line on a local machine with the usage "python app.py [-d] [-p PORT]". The -d argument should be True or False based on if you want Flask to run in debugging mode - the application will be allowed to execute arbitrary Python code on your computer. If you're in debugging mode, the app will also print out a log of the functions it's using and associated times (in seconds) that they start. The -p PORT argument determines on which port to mount the app when it runs locally.


<h4> Define and use a custom class (okay to inherit from something else, as in wxpython). </h4>

There are two custom classes defined in data/data_classes.py. 

The first one is Topic, which stores information about a particular conversation topic (topic name, topic ID, author, category, subcategories), and also has a couple methods for managing messages related to a topic (get_messages and add_message). The method get_num_pages checks how many messages are associated with the topic and returns the number of pages needed to hold them.

The other one is Message, which simply stores information about a particular message (message ID, message, author).

<h4> Define at least one magic method. </h4>

Each of the custom classes described above have init, repr, and eq methods. 

<h4> Use at least two of the following modules: itertools, random, re, os </h4>

In app.py, I used <b>os</b> to add the relative path /data to the system path. In particular, os was used to grab the current directory name, and then /data was appended to that path, which was added to the system path. This allowed me to store python modules in /data. 

Also in app.py, I used <b>itertools</b> to islice messages onto the correct pages corresponding to a topic. If there are more than 5 messages, islice selects the five (or fewer) that should be present on the current page.

<h4> Define and use a custom decorator. </h4>

My custom decorator is defined in /data/utils.py. It is a debugger decorator, with which I decorated all non-routing functions. If the -d flag is used when running the app, this will result in those decorated functions printing when they are called: their name, args, and time passed since start is printed. 


<h4> Include documentation with a detailed explanation of how to use your app. Be sure to point out anything especially cool that you did! </h4>

This document explains usage of the app. The most relevant features to note:

<ul>
	<li>Use of PostgreSQL usage to persistently store all data
	<li>Full integration and functionality with live Heroku app
	<li>Fully up and running on Heroku
	<li>Page counter / slicer is pretty cool
</ul>


<h2> Development Process </h2>

I began by sketching out my vision for the product before beginning any coding. Using my final proposal as a guide, I hashed out the goal of the product, a hierarchy of categories I planned to integrate, and a map of general site flow. I split the work I would have to do into stages:

1) Review material from class (e.g. Flask, SQL) <br>
2) Research where to host the app (I eventually came up with Heroku) <br>
3) Review and learn the relevant SQL (Heroku came with a PostgreSQL addon, so I used that) <br>
4) Write the Flask routing code for navigating through the categories <br>
5) Integrate / link together buttons on the various pages so that one could navigate through the categories <br>
6) Implement use of databases to store and display all the relevant data <br>
7) Enable ability for end-user to add to the databases through post topic/message system <br>
8) Review the final project specifications and add any features that did not come naturally through the development thus far <br>
9) Implement Bootstrap to make everything look nice <br>

I ended up following this process fairly well through step 8 - unfortunately I did not find the time to get through step 9, the addition of Bootstrap (I am unsure how easily it is implemented, as I have not used it before). 

I did not encounter any major walls throughout my development process. There were small hurdles relevant to each of the major aspects - Flask, SQL, and Heroku - that I passed by reviewing documentation and class notes. On the whole, I put about 19 hours of work into this project as it stands at submission.

<h2> Database Structure </h2>


Table: <i>topics</i> <br>
&nbsp;&nbsp;&nbsp;&nbsp;topic_id - bigint<br>
&nbsp;&nbsp;&nbsp;&nbsp;topic_name - varchar(128)<br>
&nbsp;&nbsp;&nbsp;&nbsp;author - varchar(32)<br>
&nbsp;&nbsp;&nbsp;&nbsp;category - varchar(32)<br>
&nbsp;&nbsp;&nbsp;&nbsp;subcat1 - varchar(32)<br>
&nbsp;&nbsp;&nbsp;&nbsp;subcat2 - varchar(32)<br>
&nbsp;&nbsp;&nbsp;&nbsp;subcat3 - varchar(32)<br>


Table: <i>messages</i> <br>
&nbsp;&nbsp;&nbsp;&nbsp;message_id - bigint<br>
&nbsp;&nbsp;&nbsp;&nbsp;author - varchar(32) <br>
&nbsp;&nbsp;&nbsp;&nbsp;message - text<br>
&nbsp;&nbsp;&nbsp;&nbsp;topic_id (foreign key dependent on topics.topic_id) - bigint<br>


<h2> Next Steps </h2>

I hope to continue this project over winter break - the next step is to integrate Bootstrap into it, so that it actually looks nice and is usable. Beyond that, some basic admin functions (e.g. delete responses or topics) would be useful, along with various features like displaying a preview of the latest post associated with a topic, the number of posts associated with a topic, having a widget on the homepage that points out hot topics, etc.


<h2> References </h2>

https://devcenter.heroku.com/articles/getting-started-with-python-o - Setting up Flask to work with Heroku

https://docs.python.org/3/ - Python Docs

http://www.postgresql.org/docs/ - Postgresql Docs
