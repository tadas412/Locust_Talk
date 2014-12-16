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

categories = {  # hierarchy in dictionary form
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

# ###### Database overhead #######

import os
import psycopg2
import urlparse
from data_classes import *

DB_URL = "postgres://lgkwmidyijnter:pk6dLPvtxbdcQkSJwAO37wWyUs@ec2-174-129\
-218-200.compute-1.amazonaws.com:5432/d3fh8us93rc8er"

urlparse.uses_netloc.append("postgres")
try:
    url = urlparse.urlparse(os.environ["DATABASE_URL"])  # used when on heroku
except KeyError:
    url = urlparse.urlparse(DB_URL)

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# ###### End Database overhead #######


# Returns the options that should be on the navbar
@utils.debug
def navbar_categories():
    return ["Home"] + get_high_categories() + ["About Us"]


# Returns the highest level of categories
@utils.debug
def get_high_categories():
    return categories.keys()


# Returns a string joined by /'s for the path
@utils.debug
def determine_path(*cat_list):
    try:
        path = cat_list[0]
    except IndexError:
        print "WARNING: determine_path index error"
    if path not in get_high_categories():
        return None  # invalid top level category
    for val in cat_list[1:]:
        if not val:
            break
        path = "/".join([path, val])
    return path


# Given a high level category and set of subcategories,
# returns the next level of hierarchy tree
@utils.debug
def determine_cats(category, *subcat_list):
    if not category:
        return None
    try:
        cats = categories[category.encode('ascii', 'ignore')]
    except KeyError:
        print "WARNING: determine_cats key error"
        return None

    for val in subcat_list:
        if not cats:
            return None  # We're at a leaf in the tree
        if not val:
            break  # Need to return the node of the current tree
        cats = cats[val.encode('ascii', 'ignore')]
    return cats.keys()


# Returns the Topics that should be displayed in the given category/subcat path
@utils.debug
def determine_topics(category, *subcat_list):
    if len(subcat_list) != 3:
        print "WARNING: subcat_list not length 3"  # shouldn't occur
    query = "SELECT topic_name, topic_id, author FROM topics WHERE \
             category = \'" + category + "\'"
    for i, val in enumerate(subcat_list):  # accounting for Nones
        query += " AND subcat{0} ".format(i+1)
        addition = "IS NULL" if not val else " = \'{0}".format(val) + "\'"
        query += addition

    cursor = conn.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()

    results = []
    for result in query_results:
        try:
            results.append(Topic(conn, result[0], result[1],
                           result[2]))  # converts sql output to python class
        except IndexError:
            print "WARNING: index error in determine_topics"
    return results


# Returns the Messages associated with a particular topic_id
# (returns empty Topic if it can't find it)
@utils.debug
def get_messages(topic_id):
    cursor = conn.cursor()
    cursor.execute("SELECT message_id, message, author FROM \
                    messages WHERE topic_id = %s", (topic_id,))
    query_results = cursor.fetchall()
    cursor.close()

    if not query_results:
        return None
    results = []
    for result in query_results:
        try:
            results.append(Message(result[0], result[1], result[2]))
        except IndexError:
            print "WARNING: index error in get_messages"
    return results


# Returns a Topic given a topic_id (returns an empty Topic if it can't find it)
@utils.debug
def get_topic_by_id(topic_id):
    cursor = conn.cursor()
    cursor.execute("SELECT topic_name, topic_id, author, category, \
                    subcat1, subcat2, subcat3 FROM topics WHERE \
                    topic_id = %s", (topic_id,))
    query_results = cursor.fetchone()
    cursor.close()

    if not query_results:
        return Topic(None, None, None, None)
    try:
        topic = Topic(conn, query_results[0], query_results[1],
                      query_results[2], query_results[3],
                      query_results[4], query_results[5],
                      query_results[6])
    except IndexError:
        print "WARNING: index error in get_topic_by_id"
    return topic


# Attemps to add a message to the database
@utils.debug
def add_message(topic_id, author, message):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (author, message, topic_id) \
                    VALUES(%s, %s, %s);", (author, message, topic_id))
    conn.commit()
    cursor.close()


# Attemps to add a topic to the database
@utils.debug
def add_topic(author, topic_name, path):
    cats = path.split('/')
    category = cats[0]
    subcats = [val for val in cats[1:]]
    subcats.extend([None for i in range(3 - len(subcats))])

    cursor = conn.cursor()
    cursor.execute("INSERT INTO topics (topic_name, category, author, subcat1, \
                   subcat2, subcat3) VALUES(%s, %s, %s, %s, %s, %s);",
                   (topic_name, category, author, subcats[0], subcats[1],
                    subcats[2]))
    conn.commit()
    cursor.close()
