# Definition of .filter()

# .filter() is a queryset method in Django ORM.
# it is used to get multiple records that match a condition from DB.
# It always returns a QuerySet (a list-like object), even if only one record matches.
# Unlike .get(), it does not raise an error if no records are found → it just returns an empty QuerySet.



# 👉 Key Difference vs .get():
# .get() → exactly one object (error if none or more than one).
# .filter() → zero, one, or many objects (always returns QuerySet)