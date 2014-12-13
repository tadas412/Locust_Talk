Locust Talk
========

Web app that allows visitors to post messages on a message board.

<h2> Overview </h2>

<h2> Features </h2>

<h2> Design Process </h2>

<h2> Database Structure </h2>


topics
	topic_id
	topic_name
	author
	category
	subcat1
	subcat2
	subcat3


messages
	message_id
	author
	message
	topic_id (foreign key dependent)


All varchar(32), varchar(128), or bigint

<h2> CIS 192 Final Project Requirements </h2>

<i> Your app should be callable from the command line, and should take as input at least two arguments/flags that determine its usage, which you should consume using the optparse module. </i>

Locust Talk is callable from the command line on a local machine with the usage "python app.py [debug?] [port #]". The debug argument should be True or False based on if you want Flask to run in debugging mode - the application will be allowed to execute arbitrary Python code on your computer. The port # argument determines on which port to mount the app when it runs.


<i> Define and use a custom class (okay to inherit from something else, as in wxpython). </i>

Custom classes for handling data.

<i> Define at least one magic method. </i>

The data handling custom classes each have a repr and and iter function.

<i> Use at least two of the following modules: itertools, random, re, os </i>

Use os to allow importing of files outside the current directory.
Use itertools to...

<i> Define and use a custom decorator. </i>
◦ (If you get stuck here, you can write one that does not contribute functionality to your app, but provides some “auxiliary” statistics, such as counting, timing, or debugging your functions.)

Adds debugging, which can be set up using a cmd line argument.

<i> Include documentation with a detailed explanation of how to use your app. Be sure to point out anything especially cool that you did! </i>

This document explains usage of the app. Some cool things:

Cache system for handling data using appropriate datastructures.
Fully up and running on Heroku




<h2> References </h2>

https://devcenter.heroku.com/articles/getting-started-with-python-o - Setting up Flask to work with Heroku
