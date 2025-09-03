# 🔹 What is exclude()?
# it is a queryset method in django ORM 
# exclude() is the opposite of filter().
# It retrieves all records except the ones that match the condition.
# Think of it like:
# 👉 "Give me everything, but NOT this..."



# 🔹 Examples of exclude()
# 1. Exclude by exact value
# Profile.objects.exclude(role="admin")
# 👉 Returns all profiles except admins (only students).

# 2. Exclude multiple values
# Profile.objects.exclude(department__in=["IT", "CS"])
# 👉 Returns all students not in IT or CS department.

# 3. Exclude with contains
# Profile.objects.exclude(name__icontains="ash")
# 👉 Returns all profiles where the name does NOT contain "ash".

# 4. Exclude by year
# Profile.objects.exclude(year_of_admission__lt=2020)
# 👉 Returns students who were admitted in 2020 or later (excludes before 2020).

# 5. Chain with filter
# Profile.objects.filter(department="IT").exclude(year_of_admission__lt=2022)
# 👉 Returns IT students, but excludes those admitted before 2022.
# ✅ Summary
# filter() = get records matching condition.
# exclude() = get records NOT matching condition.
# Both can be chained together for precise queries.