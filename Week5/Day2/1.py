# 🔹 1. aggregate()
# it travel thorogh each value 
# Returns a single dictionary with aggregated values.
# note:return dict.
# Example:
# from django.db.models import Count, Avg, Max, Min

# # Total number of users
# User.objects.aggregate(total=Count('id'))
# # 👉 {'total': 5}
# # Average age of users
# User.objects.aggregate(avg_age=Avg('age'))
# # 👉 {'avg_age': 29}
# # Maximum & Minimum age
# User.objects.aggregate(max_age=Max('age'), min_age=Min('age'))
# # 👉 {'max_age': 40, 'min_age': 25}
# 👉 aggregate() = overall summary of the entire table/queryset.



# 2. annotate()
# Works on each row of the queryset.(like a GROUP BY in sql)
# Adds an extra calculated field to each object.

# Example 1: Count related objects
# Suppose we have:
# class User(models.Model):
#     name = models.CharField(max_length=100)

# class Note(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
#     content = models.TextField()


# Now count notes per user:
# from django.db.models import Count
# users = User.objects.annotate(note_count=Count('notes'))
# for u in users:
#     print(u.name, u.note_count)


# 👉 Output:
# John   3
# Alice  5
# Bob    0
# Here, note_count is added to each user row.


# Example 2: Annotate with Avg
# from django.db.models import Avg
# users = User.objects.annotate(avg_length=Avg('notes__content__length'))
# for u in users:
#     print(u.name, u.avg_length)
# 👉 Each user gets their own average note length.

# 🔹 Key Difference
# Feature	             aggregate()	            annotate()
# Scope	             Whole queryset (summary)	Per row (or group)
# Return type	         Dictionary	                QuerySet
# Example usage	     Total users, average age	Notes per user, orders per customer
# Output count	     Always 1 row	            Same as queryset rows

# ✅ Think like this:
# aggregate() → "Give me one number (summary)"
# annotate() → "Add a new number to each row (extra info)"