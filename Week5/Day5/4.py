# Django ORM vs Raw SQL – Aggregates
# 1. SUM()
# 🔹 Raw SQL
# SELECT SUM(salary) FROM Employee;

# 🔹 Django ORM
# from django.db.models import Sum
# Employee.objects.aggregate(total_salary=Sum("salary"))
# # {'total_salary': 250000}

# 2. COUNT()
# 🔹 Raw SQL
# SELECT COUNT(*) FROM Employee WHERE department = 'IT';

# 🔹 Django ORM
# from django.db.models import Count
# Employee.objects.filter(department="IT").aggregate(count=Count("id"))
# # {'count': 10}

# 3. AVG()
# 🔹 Raw SQL
# SELECT AVG(salary) FROM Employee;

# 🔹 Django ORM
# from django.db.models import Avg
# Employee.objects.aggregate(avg_salary=Avg("salary"))
# # {'avg_salary': 50000.0}

# 4. MAX()
# 🔹 Raw SQL
# SELECT MAX(salary) FROM Employee;

# 🔹 Django ORM
# from django.db.models import Max
# Employee.objects.aggregate(max_salary=Max("salary"))
# # {'max_salary': 90000}

# 5. MIN()
# 🔹 Raw SQL
# SELECT MIN(salary) FROM Employee;

# 🔹 Django ORM
# from django.db.models import Min
# Employee.objects.aggregate(min_salary=Min("salary"))
# # {'min_salary': 30000}

# Extra – GROUP BY Equivalent
# Sometimes you’ll also want to group by department (like SQL GROUP BY):

# 🔹 Raw SQL
# SELECT department, AVG(salary) 
# FROM Employee 
# GROUP BY department;


# 🔹 Django ORM
# Employee.objects.values("department").annotate(avg_salary=Avg("salary"))
# # [{'department': 'IT', 'avg_salary': 60000}, {'department': 'HR', 'avg_salary': 45000}]


# ✅ Summary Table
# SQL Function	Django ORM Equivalent
# SUM(col)	.aggregate(Sum("col"))
# COUNT(col)	.aggregate(Count("col"))
# AVG(col)	.aggregate(Avg("col"))
# MAX(col)	.aggregate(Max("col"))
# MIN(col)	.aggregate(Min("col"))
# GROUP BY	.values("field").annotate(...)