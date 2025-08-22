# 🔥 CASCADE in SQL (especially PostgreSQL):
# 👉 What it does:
# When you use CASCADE with DROP, it not only deletes the main object (like a table),
# but also deletes all other dependent objects automatically. 



# 🔹 What is SERIAL?
# SERIAL is a special data type in PostgreSQL (and some other SQL databases).
# It is used to create a unique auto-incrementing integer column (usually for id/primary key).
# When you insert a new row, you don’t need to give a value for that column — SQL will automatically assign the next number.


# 🔹 Key Point
# 👉 SERIAL is not part of the SQL standard.
# In standard SQL / MySQL you use:
    
# AUTO_INCREMENT (MySQL)
# IDENTITY (SQL Server)



# | Feature           | `WHERE`                               | `HAVING`                              |
# | ----------------- | ------------------------------------- | ------------------------------------- |
# | 📌 Used for       | Filtering **rows** (before grouping)  | Filtering **groups** (after grouping) |
# | 📦 Works on       | Individual rows                       | Aggregated/grouped data               |
# | 🔢 Can use COUNT? | ❌ No (cannot use aggregate functions) | ✅ Yes (can use COUNT, SUM, etc.)      |
# | 🔁 Used with      | Any `SELECT`                          | Usually used with `GROUP BY`          |
