# Definition: Combines rows from two or more tables based on a related column.

# 🔹 Sample Tables

# users
# id	name	age	place
# 1	Samadev	20	KasarGod
# 2	Anas	50	Kerala
# 3	Afnas	150	Kannur
# 4	John	25	Mumbai

# address
# id	place	pincode
# 1	Kerala	652306
# 2	KasarGod	612306
# 3	Kannur	624306
# 4	Kozhikode	644402

# 1️⃣ INNER JOIN
# 👉 Returns only rows that match in both tables.
# SELECT u.id, u.name, u.age, u.place, a.pincode
# FROM users u
# INNER JOIN address a
# ON u.place = a.place;


# Result:
# id	name	age	place	pincode
# 1	Samadev	20	KasarGod	612306
# 2	Anas	50	Kerala	652306
# 3	Afnas	150	Kannur	624306

# ❌ John (Mumbai) and Kozhikode don’t appear because they don’t match.

# 2️⃣ LEFT JOIN
# 👉 Returns all users + matching addresses. If no match, address columns are NULL.
# SELECT u.id, u.name, u.age, u.place, a.pincode
# FROM users u
# LEFT JOIN address a
# ON u.place = a.place;


# Result:
# id	name	age	place	pincode
# 1	Samadev	20	KasarGod	612306
# 2	Anas	50	Kerala	652306
# 3	Afnas	150	Kannur	624306
# 4	John	25	Mumbai	NULL


# 3️⃣ RIGHT JOIN
# 👉 Returns all addresses + matching users. If no match, user columns are NULL.
# SELECT u.id, u.name, u.age, a.place, a.pincode
# FROM users u
# RIGHT JOIN address a
# ON u.place = a.place;

# Result:
# id	name	age	place	pincode
# 1	Samadev	20	KasarGod	612306
# 2	Anas	50	Kerala	652306
# 3	Afnas	150	Kannur	624306
# NULL	NULL	NULL	Kozhikode	644402

# 4️⃣ FULL OUTER JOIN
# 👉 Returns all rows from both tables. If no match, missing side is NULL.
# SELECT u.id, u.name, u.age, u.place, a.pincode
# FROM users u
# FULL OUTER JOIN address a
# ON u.place = a.place;


# Result:
# id	name	age	place	pincode
# 1	Samadev	20	KasarGod	612306
# 2	Anas	50	Kerala	652306
# 3	Afnas	150	Kannur	624306
# 4	John	25	Mumbai	NULL
# NULL	NULL	NULL	Kozhikode	644402

# 5️⃣ CROSS JOIN
# 👉 Combines every user with every address (cartesian product).
# SELECT u.id, u.name, u.place, a.place, a.pincode
# FROM users u
# CROSS JOIN address a;
# Result: (just a few rows shown)

# id	name	user_place	addr_place	pincode
# 1	Samadev	KasarGod	Kerala	652306
# 1	Samadev	KasarGod	KasarGod	612306
# 1	Samadev	KasarGod	Kannur	624306
# …	…	…	…	…

# 👉 If users has 4 rows and address has 4 rows → result = 16 rows.
# 🔑 Summary
# INNER JOIN → Only matches
# LEFT JOIN → All users + matches
# RIGHT JOIN → All addresses + matches
# FULL OUTER JOIN → All users + all addresses
# CROSS JOIN → Every possible combination