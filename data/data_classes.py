import utils


# Represents a single topic in the forum
class Topic:

    def __init__(self, conn, topic_name, topic_id, author,
                 category=None, subcat1=None, subcat2=None, subcat3=None):
        self.conn = conn
        self.topic_name = topic_name
        self.topic_id = topic_id
        self.author = author
        self.category = category
        self.subcat1 = subcat1
        self.subcat2 = subcat2
        self.subcat3 = subcat3

    # Allows for printing
    def __repr__(self):
        return self.topic_name

    # Allows for == comparison
    def __eq__(self, topic):
        if not self or not topic:
            return False
        try:
            return self.topic_id == topic.topic_id
        except:
            return False

    # Returns the number of pages needed to display in groups of 5
    @utils.debug
    def get_num_pages(self):
        if not self.topic_id:
            print "WARNING: get_num_pages called without setting topic_id"
            return 0

        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM messages WHERE topic_id = %s;",
                       (self.topic_id,))
        try:
            result = int(cursor.fetchone()[0])
        except (ValueError, KeyError):
            print "WARNING: get_num_pages had bad query response"
            result = 0
        cursor.close()
        return (result / 5) if (result % 5 == 0) else (result / 5 + 1)

    # Returns the messages associated. Requires topic_id to be set.
    @utils.debug
    def get_messages(self):
        if not self.topic_id:
            print "WARNING: get_messages called without setting topic_id"
            return []
        cursor = self.conn.cursor()
        cursor.execute("SELECT message_id, message, author FROM messages \
                        WHERE topic_id = %s", (self.topic_id,))
        query_results = cursor.fetchall()
        cursor.close()

        if not query_results:
            return []
        results = []
        for result in query_results:
            results.append(Message(result[0], result[1], result[2]))
        return results

    # Adds a message to the topic
    @utils.debug
    def add_message(self, author, message):
        if not self.topic_id:
            print "WARNING: add_message called without setting topic_id"
            return None

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO messages (author, message, topic_id) \
                        VALUES(%s, %s, %s);", (author, message, self.topic_id))
        self.conn.commit()
        cursor.close()


# Represents a single message in the forum
class Message:

    def __init__(self, message_id, message, author):
        self.message_id = message_id
        self.message = message
        self.author = author

    # Allows for printing
    def __repr__(self):
        return self.message

    # Allows for == comparison
    def __eq__(self, message):
        if not self or not message:
            return False
        try:
            return self.message_id == message.message_id
        except:
            return False
