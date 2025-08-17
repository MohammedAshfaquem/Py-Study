✅ What is a View in SQL?
A View is like a virtual table.
It doesn't store data, but shows data from one or more real tables using a saved SQL query.


| Benefit                | What it Means                                      |
| -------------------  - | -------------------------------------------------- |
| ✅ Simplifies Queries | Hide complex joins or filters behind a simple name |
| ✅ Better Security    | Expose only certain columns or rows to users       |
| ✅ Reusability        | Use the same logic/query in many places            |
| ✅ Readable Code      | Keeps your main queries clean and readable         |




| Term   | Meaning                        |
| ------ | ------------------------------ |
| `VIEW` | A saved SELECT query           |
| Use    | To simplify, secure, reuse SQL |
| Create | `CREATE VIEW view_name AS ...` |
| Use it | `SELECT * FROM view_name;`     |

    
    
EG:📋 Example Tables
🟦 users table:
id	name	age
1	Akshay	24
2	Priya	30


🟨 orders table:
id	user_id	product
1	1	Laptop
2	2	Mouse


🔧 Create a View
🎯 Goal: Create a view that shows users and their orders
CREATE VIEW user_orders AS
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id;


✅ This creates a virtual table called user_orders.
🔎 Use the View Like a Table
Now you can query it just like a normal table:
SELECT * FROM user_orders;
Result:
name	product
Akshay	Laptop
Priya	Mouse
