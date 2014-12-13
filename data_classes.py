class Topic:

	def __init__(self, conn, topic_name, topic_id, author, category=None, subcat1=None, subcat2=None, subcat3=None):
		self.conn = conn
		self.topic_name = topic_name
		self.topic_id = topic_id
		self.author = author
		self.category = category
		self.subcat1 = subcat1
		self.subcat2 = subcat2
		self.subcat3 = subcat3

	def __repr__(self):
		return self.topic_name

	def __eq__(self, topic):
		if not self or not topic:
			return False
		try:
			return self.topic_id == topic.topic_id
		except:
			return False

	# Requires topic_id to be set
	def get_messages(self):
		print "getting message"
		if not self.topic_id:
			print "WARNING: get_messages called without setting topic_id"
			return None
		cursor = self.conn.cursor()
		cursor.execute("SELECT message_id, message, author FROM messages WHERE topic_id = %s", (self.topic_id,))
		query_results = cursor.fetchall()
		cursor.close()
	
		if not query_results:
			return None
		results = []
		for result in query_results:
			results.append(Message(result[0], result[1], result[2]))
		return results

	def add_message(self, author, message):
		print "adding message"
		if not self.topic_id:
			print "WARNING: add_message called without setting topic_id"
			return None

		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO messages (author, message, topic_id) VALUES(%s, %s, %s);", (author, message, self.topic_id))
		self.conn.commit()
		cursor.close()


class Message:

	def __init__(self, message_id, message, author):
		self.message_id = message_id
		self.message = message
		self.author = author

	def __repr__(self):
		return self.message

	def __eq__(self, message):
		if not self or not message:
			return False
		try:
			return self.message_id == message.message_id
		except:
			return False

			