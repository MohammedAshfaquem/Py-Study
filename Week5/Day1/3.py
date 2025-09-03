# 🔹 What are Query Lookups?
# Query lookups are extra conditions you can add when filtering data with .filter() or .exclude().
# They let you check things like:
# exact match
# contains text
# greater than / less than
# date ranges
# case-insensitive search, etc.


# 🔹 Common Query Lookups
# 1. Exact match
# Profile.objects.filter(name__exact="Ashfaque")
# 👉 Returns users whose name is exactly "Ashfaque".

# 2. Case-insensitive exact
# Profile.objects.filter(name__iexact="ashfaque")
# 👉 Returns "Ashfaque", "ASHFAQUE", "ashfaque" (ignores case).

# 3. Contains
# Profile.objects.filter(name__contains="ash")
# 👉 Finds names that contain "ash" (case-sensitive).
# Example: "Ashfaque", "Hashim".

# 4. Case-insensitive contains
# Profile.objects.filter(name__icontains="ash")
# 👉 Same as above but ignores case.
# Example: "ashfaque", "ASHWIN", "Hashim".

# 5. Startswith / Endswith
# Profile.objects.filter(name__startswith="Mo")
# Profile.objects.filter(name__endswith="que")
# 👉 Finds names starting with "Mo" or ending with "que".

# 6. Greater than / Less than
# Profile.objects.filter(year_of_admission__gt=2020)  # greater than 2020
# Profile.objects.filter(year_of_admission__lt=2020)  # less than 2020

# 7. Range
# Profile.objects.filter(year_of_admission__range=(2018, 2022))
# 👉 Finds students admitted between 2018 and 2022.

# 8. In
# Profile.objects.filter(department__in=["IT", "CS"])
# 👉 Finds students from either IT or CS.

# 9. Date lookups
# If date_of_birth is a DateField:
# Profile.objects.filter(date_of_birth__year=2000)
# Profile.objects.filter(date_of_birth__month=9)
# Profile.objects.filter(date_of_birth__day=2)
# 👉 Filters by year, month, or day.

# Syntax:
# field__lookup=value