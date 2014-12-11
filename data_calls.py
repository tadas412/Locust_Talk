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
	# TODO - going to need to return objects that have names, IDs, stats, etc
	return ["ferguson incident", "PILOTs"]