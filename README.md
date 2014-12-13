Locust Talk
========

Web app that allows visitors to post messages on a message board.

<h2> Overview </h2>

<h2> Features </h2>

<h2> CIS 192 Final Project Requirements </h2>

<h3> Your app should be callable from the command line, and should take as input at least two arguments/flags that determine its usage, which you should consume using the optparse module. </h3>

Locust Talk is callable from the command line on a local machine with the usage "python app.py [-d] [-p PORT]". The -d argument should be True or False based on if you want Flask to run in debugging mode - the application will be allowed to execute arbitrary Python code on your computer. If you're in debugging mode, the app will also print out a log of the functions it's using and associated times (in seconds) that they start. The -p PORT argument determines on which port to mount the app when it runs locally.


<h3> Define and use a custom class (okay to inherit from something else, as in wxpython). </h3>

There are two custom classes defined in data/data_classes.py. 

The first one is Topic, which stores information about a particular conversation topic (topic name, topic ID, author, category, subcategories), and also has a couple methods for managing messages related to a topic (get_messages and add_message).

The other one is Message, which simply stores information about a particular message (message ID, message, author).

<h3> Define at least one magic method. </h3>

Each of the custom classes have init, repr, and eq methods. 

<h3> Use at least two of the following modules: itertools, random, re, os </h3>

Use os to allow importing of files outside the current directory.
Use itertools to islice up the pages by 5 messages. (describe in detail)

<h3> Define and use a custom decorator. </h3>
◦ (If you get stuck here, you can write one that does not contribute functionality to your app, but provides some “auxiliary” statistics, such as counting, timing, or debugging your functions.)

Adds debugging to non-routing function calls, which can be set up using the cmd line argument -d.

<h3> Include documentation with a detailed explanation of how to use your app. Be sure to point out anything especially cool that you did! </h3>

This document explains usage of the app. Some cool things, besides what's described above...

SQL implementation
Fully up and running on Heroku
Page counter / slicer is pretty cool


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




<h2> References </h2>

https://devcenter.heroku.com/articles/getting-started-with-python-o - Setting up Flask to work with Heroku

Python Docs

Postgresql Docs
