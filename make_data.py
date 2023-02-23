#i/User/bin/env

import sqlite3

conn = sqlite3.connect('social_media.db')
c = conn.cursor()

c.execute("""CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  email TEXT NOT NULL
  )
  """
)
c.execute("""CREATE TABLE followers (
  user_id INTEGER PRIMARY KEY,
  follower_id TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (follower_id) REFERENCES users(id)
  )
  """
)
c.execute("""CREATE TABLE follows (
  user_id INTEGER PRIMARY KEY,
  following_id TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (following_id) REFERENCES users(id)
  )
  """
)

c.execute("""CREATE TABLE posts (
  id INTEGER PRIMARY KEY, 
  user_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
  """
)

c.execute("""CREATE TABLE comments (
  id INTEGER PRIMARY KEY,
  post_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  parent_id INTEGER, -- this is a id of a user
  FOREIGN KEY (post_id) REFERENCES posts(id),
  FOREIGN KEY (parent_id) REFERENCES comments(id)
  )
"""
)
conn.commit()
