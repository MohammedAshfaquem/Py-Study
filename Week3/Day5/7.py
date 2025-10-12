# 🔹 1. DECLARE in SQL
# DECLARE is used to define variables,or conditions in SQL.
# especially inside  functions, or scripts.


# 🔹 2. What is a Cursor?
# A cursor is a temporary pointer  that allows row-by-row processing of a query result set.

# 🔑 Why use cursors?
# Normally, SQL operates on sets (multiple rows at once).
# But sometimes, you need to handle each row individually — that’s where cursors come in.

# 🔁 Steps to Use a Cursor:
# 1. DECLARE the cursor
# Define the SQL query and give the cursor a name.

# 2. OPEN the cursor
# Execute the query and populate the cursor.

# 3. FETCH rows from the cursor
# Retrieve rows one at a time.

# 4. CLOSE the cursor
# Release the result set.

# 5. DEALLOCATE the cursor
# Completely remove it from memory.



# ⚠️ Drawbacks of Cursors:
# Slower than set-based queries (like UPDATE, SELECT, etc.)
# More resource-intensive
# Use only when necessary


# | Term       | Meaning                                                   |
# | ---------- | --------------------------------------------------------- |
# | `DECLARE`  | Used to define variables, cursors, or control handlers    |
# | **Cursor** | A pointer to loop through query results one row at a time |
