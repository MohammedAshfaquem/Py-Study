# 🔹 Django Cursor (for raw SQL)
# Sometimes, instead of using raw() or ORM, we may want to execute custom SQL queries directly.
# For that, Django provides a cursor object through the database connection.


# 1. How to Get a Cursor
# from django.db import connection
# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM myapp_employee WHERE salary < %s", [80000])
#     rows = cursor.fetchall()
    
# 👉 Here:
# connection.cursor() → gives you a DB cursor.
# cursor.execute(sql, params) → safely executes query (params prevent SQL injection).
# cursor.fetchall() → returns all rows.

# 2. Fetching Results
# You have 3 main fetch methods:
# cursor.fetchone()   # Get a single row
# cursor.fetchall()   # Get all rows
# cursor.fetchmany(n) # Get n rows

# 3. Example: Insert, Update, Delete
# with connection.cursor() as cursor:
#     # Insert
#     cursor.execute(
#         "INSERT INTO myapp_employee (name, salary, managerId) VALUES (%s, %s, %s)",
#         ["John", 75000, 3]
#     )

#     # Update
#     cursor.execute(
#         "UPDATE myapp_employee SET salary = %s WHERE id = %s",
#         [90000, 1]
#     )

#     # Delete
#     cursor.execute(
#         "DELETE FROM myapp_employee WHERE salary < %s",
#         [50000]
#     )

# 4. Why Use Cursor Instead of ORM?
# ✅ When ORM cannot express complex SQL easily.
# ✅ When you want raw speed (e.g., bulk operations).
# ✅ When you’re using DB-specific features (like PostgreSQL extensions, stored procedures, etc.).

# 5. Important Notes
# Always use parameterized queries (%s) → prevents SQL injection.
# Always use with connection.cursor() → it automatically closes the cursor.
# Cursor returns tuples by default, not dictionaries.

# Example: ("Joe", 70000, 3) instead of {"name": "Joe", "salary": 70000}.
# 👉 If you want dict-like results, you can use DictCursor in some cases (depends on backend).