"""
	PATH BREAKDOWN:

	Locust_Talk
		Academics
			Profs and Classes
			Majors/Minors
		Career
			Events
			Internship Discussion
			Full-Time Discussion
			Networking Opportunities
		Intellectual Discussion
		Extracurricular Activities
			Club Advertising
		Campus Events
		Social Life
			Senior Societies
			Greek Life
				Events
"""

categories = {
	"academics": {
		"profs_and_classes": None,
		"majors_and_minors": None
	},
	"career": {
		"events": None,
		"internship_discussion": None,
		"full-time_discussion": None,
		"networking_opportunities": None
	},
	"intellectual_discussion": None,
	"extracurricular_activities": {
		"club_advertising": None
	},
	"campus_events": None,
	"social_life": {
		"senior_societies": None,
		"greek_life": {
			"events": None
		}
	}
}

# Database overhead

import os
import psycopg2
import urlparse
from data_classes import *

urlparse.uses_netloc.append("postgres")
try:
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
except:
	url = urlparse.urlparse("postgres://lgkwmidyijnter:pk6dLPvtxbdcQkSJwAO37wWyUs@ec2-174-129-218-200.compute-1.amazonaws.com:5432/d3fh8us93rc8er")

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

def navbar_categories():
	return ["Home"] + get_high_categories() + ["About Us"]

def get_high_categories():
	return categories.keys()

def determine_path(*cat_list):
	path = cat_list[0]
	for val in cat_list[1:]:
		if not val: break
		path = "/".join([path, val])
	return path


def determine_cats(category, *subcat_list):
	if not category:
		return None
	cats = categories[category.encode('ascii', 'ignore')]
	for val in subcat_list:
		if not cats:
			return None # We're at a leaf in the tree
		if not val:
			break # Need to return the node of the current tree
		cats = cats[val.encode('ascii', 'ignore')]
	return cats.keys()

def determine_topics(category, *subcat_list):
	# pull from db using category, subcat_list, to return list of topic name strings
	# afterward, change to returning an object (i.e. class) that has at least topic name, topic id
	if len(subcat_list) != 3:
		print "WARNING: subcat_list not length 3"
	query = "SELECT topic_name, topic_id, author FROM topics WHERE category = \'" + category + "\'"
	for i, val in enumerate(subcat_list):
		query += " AND subcat{0} ".format(i+1)
		addition = "IS NULL" if not val else  " = \'{0}".format(val) + "\'"
		query += addition

	cursor = conn.cursor()
	cursor.execute(query)
	query_results = cursor.fetchall();
	print query_results
	results = []
	for result in query_results:
		results.append(Topic(result[0], result[1], result[2]))
	cursor.close()
	return results



