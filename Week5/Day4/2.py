# 🟢 What is raw() in Django?
# Normally in Django you use the ORM
# But sometimes you want to write pure SQL.
# For that, Django gives you:
# here we can only fetch data INSER,UPDATE,DELETE is not possible.
# Signals: ❌ Not triggered
# Model.objects.raw("YOUR_SQL_QUERY")


# 👉 raw() lets you run raw SQL queries while still returning model instances.

# 🟢 Using parameters (safe query)

# Instead of hardcoding values:

# salary_limit = 80000
# employees = Employee.objects.raw(
#     "SELECT * FROM myapp_employee WHERE salary < %s", [salary_limit]
# )


# %s = placeholder.

# [salary_limit] = parameters (prevents SQL injection).

# 🟢 Example with Join
# query = """
# SELECT e.id, e.name, e.salary, m.name as manager_name
# FROM myapp_employee e
# JOIN myapp_employee m ON e.managerId = m.id
# WHERE e.salary > m.salary
# """

# employees = Employee.objects.raw(query)

# for emp in employees:
#     print(emp.name, emp.salary)

# 🟢 When to use raw()?
# When ORM is too limited for a complex query.
# When you want full SQL control.
# When performance optimization is required
# 🟢 When NOT to use
# If ORM can handle it → prefer ORM (cleaner & database-agnostic).
# Harder to maintain and test.

# 👉 In short:
# raw() lets you write SQL directly but still get Django model objects back.