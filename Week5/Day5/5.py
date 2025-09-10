# 1. INNER JOIN
# 👉 Returns rows that have matching values in both tables.

# 🔹 Raw SQL
# SELECT e.name, d.name 
# FROM Employee e
# INNER JOIN Department d ON e.dept_id = d.id;


# 🔹 Django ORM
# Employee.objects.select_related("department").values("name", "department__name")

# 2. LEFT OUTER JOIN
# 👉 Returns all rows from the left table, even if there are no matches in the right.
# 🔹 Raw SQL
# SELECT e.name, d.name 
# FROM Employee e
# LEFT JOIN Department d ON e.dept_id = d.id;


# 🔹 Django ORM
# Employee.objects.select_related("department").values("name", "department__name")
# # Django always does LEFT OUTER JOIN by default when accessing FK relations.

# 3. RIGHT OUTER JOIN
# 👉 Returns all rows from the right table, even if there are no matches in the left.
# ⚠️ Django ORM does not support RIGHT JOIN directly.

# 🔹 Raw SQL
# SELECT e.name, d.name 
# FROM Employee e
# RIGHT JOIN Department d ON e.dept_id = d.id;


# 🔹 Django ORM
# # Not directly supported. You must reverse the query:
# Department.objects.prefetch_related("employee_set").values("name", "employee__name")

# 4. FULL OUTER JOIN
# 👉 Returns all rows from both tables, whether there is a match or not.
# ⚠️ Not directly supported in Django ORM (and even in MySQL). You’d use raw SQL or Union queries.
# 🔹 Raw SQL
# SELECT e.name, d.name
# FROM Employee e
# FULL OUTER JOIN Department d ON e.dept_id = d.id;


# 🔹 Django ORM (workaround)
# qs1 = Employee.objects.values("name", "department__name")
# qs2 = Department.objects.values("employee__name", "name")
# full_join = qs1.union(qs2)

# 5. SELF JOIN
# 👉 A table joined with itself.
# 🔹 Raw SQL
# SELECT e1.name AS Employee, e2.name AS Manager
# FROM Employee e1
# JOIN Employee e2 ON e1.manager_id = e2.id;


# 🔹 Django ORM
# Employee.objects.values("name", "manager__name")
# (Here, manager is a ForeignKey('self', ...) field in the Employee model.)

# ✅ Summary Table
# Join Type	Raw SQL Example	Django ORM Equivalent
# INNER JOIN	INNER JOIN	.select_related()
# LEFT OUTER JOIN	LEFT JOIN	Default ORM behavior
# RIGHT OUTER JOIN	RIGHT JOIN	Not supported directly, reverse query
# FULL OUTER JOIN	FULL JOIN	Use .union()
# SELF JOIN	JOIN same table	FK to self (manager__name)

# ⚡ Key Tip:
# Django ORM automatically uses LEFT OUTER JOIN when following relations (ForeignKey, OneToOne).
# For complex joins (RIGHT/FULL) → you often need raw SQL.