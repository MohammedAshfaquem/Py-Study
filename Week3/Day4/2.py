# 🔹 What is a Subquery?
# A subquery is a query inside another query.
# It is written inside parentheses ( ) and usually used with SELECT, INSERT, UPDATE, or DELETE.
# It’s also called:
# Inner query
# Nested query
Here Inner Query runs First After that outer query runs



# 🔹 Types of Subqueries

# | Type              | Example Keyword                   |
# | ----------------- | --------------------------------- |
# | In `WHERE` clause | `IN`, `=`, `>`, etc.              |
# | In `FROM` clause  | Used as virtual table (alias)     |
# | In `SELECT`       | Get computed values (like totals) |


# 🔹 Types of Subqueries
# 1️⃣ Subquery in WHERE clause
# Find users who live in the same places that exist in the address table:
# SELECT name, place 
# FROM users
# WHERE place IN (SELECT place FROM address);


# Here:
# (SELECT place FROM address) runs first.
# Then main query checks users.place against that list.
# ✅ Filters only users with valid address records.


# 2️⃣ Subquery in SELECT clause
# Add pincode from address table for each user (without join):
# SELECT 
#     name,
#     place,
#     (SELECT pincode FROM address a WHERE a.place = u.place) AS pincode
# FROM users u;
# The subquery runs once per row in users.

# 3️⃣ Subquery in FROM clause (Derived Table)
# You can treat a subquery as a temporary table:
# SELECT place, COUNT(*) as user_count
# FROM (
#     SELECT place FROM users
# ) AS temp
# GROUP BY place;
# This gives you user count per place.

# 4️⃣ Subquery in UPDATE
# Update user place using a value from another table:
# UPDATE users
# SET place = (
#     SELECT place FROM address WHERE pincode = 612306
# )
# WHERE id = 4;

# 🔑 Subquery vs Join
# Subquery: Runs inner query first, then outer query. Good for filtering, calculations, or nested logic.
# JOIN: Directly combines tables, usually faster for retrieving related data.
