import sqlite3

conn = sqlite3.connect('social_media.db')
c = conn.cursor()

# Insert some example posts
conn.execute("INSERT INTO posts (user_id, content) VALUES (1, 'This is post #1')")
conn.execute("INSERT INTO posts (user_id, content) VALUES (2, 'This is post #2')")
conn.execute("INSERT INTO posts (user_id, content) VALUES (1, 'This is post #3')")

# Insert some example comments
conn.execute("INSERT INTO comments (post_id, user_id, content) VALUES (1, 2, 'This is a comment on post #1')")
conn.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 1, 'This is a reply to the first comment', 1)")
conn.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 2, 'This is a reply to the reply', 2)")
conn.execute("INSERT INTO comments (post_id, user_id, content) VALUES (2, 1, 'This is a comment on post #2')")
conn.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 2, 'This is a nested reply to the first comment', 3)")
conn.execute("INSERT INTO comments (post_id, user_id, content) VALUES (1, 1, 'This is another comment on post #1')")
conn.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 2, 'This is a reply to the second comment', 6)")

conn.commit()