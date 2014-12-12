class Topic:

	def __init__(self, topic_name, topic_id, author, category=None, subcat1=None, subcat2=None, subcat3=None):
		self.topic_name = topic_name
		self.topic_id = topic_id
		self.author = author
		self.category = category
		self.subcat1 = subcat1
		self.subcat2 = subcat2
		self.subcat3 = subcat3


class Message:

	def __init__(self, message_id, message, author):
		self.message_id = message_id
		self.message = message
		self.author = author