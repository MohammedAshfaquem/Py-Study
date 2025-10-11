# What is a Manager?
# A Manager is the interface between Django models and the database.
# Every Django model gets a default manager called objects.
# we use this manager to run queries (.all(), .filter(), .get(), etc.).
# 👉 In short: Manager = entry point to ORM queries.
# 🔹 Example (default manager)
# users = User.objects.all()        # get all users
# john = User.objects.get(name="John")
# students = User.objects.filter(age__gte=18)
# Here, objects is the default manager for User.

# 🔹 Custom Managers
# we can define our own manager with extra methods to organize queries better.
# Example
# from django.db import models

# class UserManager(models.Manager):
#     def adults(self):
#         return self.filter(age__gte=18)

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     # attach custom manager
#     objects = UserManager()


# Now you can do:
# User.objects.adults()
# # 👉 Returns all users where age >= 18

# 🔹 Multiple Managers
# You can even define more than one manager:

# class ActiveUserManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)

#     objects = models.Manager()         # default
#     active = ActiveUserManager()       # custom


# Usage:
# User.objects.all()   # all users
# User.active.all()    # only active users

# 🔹 Summary
# Manager = gateway to the ORM.
# Default manager = objects.
# You can create custom managers to encapsulate common queries.
# Custom managers keep your code DRY and readable.

# ✅ Think like this:
# Model = blueprint of table.
# Manager = handle to talk to that table.
# QuerySet = actual set of rows you get back.