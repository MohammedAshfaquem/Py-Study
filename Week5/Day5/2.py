
# bulk_update() is a QuerySet method. 
# it allow us to update multiple model objects in the database at once.
# Instead of looping and calling .save() on each object, you can update them in a single query.
# This makes updates much faster when dealing with many records.

# ✅ Syntax
# Model.objects.bulk_update(objs, fields, batch_size=None)
# objs → a list of model objects you want to update.
# fields → list of field names that should be updated.
# batch_size → optional, how many objects to update per batch (useful for very large updates).

# ✅ Key Points
# Performance boost – much faster than calling .save() on each object.
# Requires PK – the objects must already exist in the database (i.e., they must have a primary key).
# No signals – just like bulk_create(), it does not trigger signals (pre_save, post_save, etc.).
# Partial updates – you must explicitly specify which fields to update (["salary"], ["name", "salary"], etc.).


# ✅ Analogy
# .save() → updating one record at a time (like editing files one by one).
# .bulk_update() → updating many records in one shot (like running a script that edits all files together).


# def Update(request):
#     std = Student.objects.all()
#     for s in std:
#         if s.name == 'Asif':
#             s.age= 100
#         elif s.name == "Anas":
#             s.age=12
#     Student.objects.bulk_update(std,fields=['age'])
#     return HttpResponse("Update Working")