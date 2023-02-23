import sqlite3

conn = sqlite3.connect('social_media.db')
c = conn.cursor()

# The post ID we want to retrieve comments for
post_id = 1

# Define the recursive query CTE
recursive_query = """
WITH RECURSIVE comment_tree(id, post_id, user_id, content, created_at, parent_id, depth) AS (
  -- Base case: select top-level comments
  SELECT id, post_id, user_id, content, created_at, parent_id, 0
  FROM comments
  WHERE post_id = ? AND parent_id IS NULL
  
  UNION ALL
  
  -- Recursive case: select nested comments
  SELECT c.id, c.post_id, c.user_id, c.content, c.created_at, c.parent_id, ct.depth + 1
  FROM comments c
  JOIN comment_tree ct ON c.parent_id = ct.id
)
SELECT id, post_id, user_id, content, created_at, parent_id, depth
FROM comment_tree
ORDER BY created_at ASC
"""


# Execute the recursive query with the post_id parameter
cursor = conn.execute(recursive_query, (post_id,))

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
  print("row:",row)


#cd mnt/c/Users/jakej/OneDrive/Documents/CS/CS-4307/