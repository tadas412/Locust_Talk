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



<h2> References </h2>

https://devcenter.heroku.com/articles/getting-started-with-python-o - Setting up Flask to work with Heroku
