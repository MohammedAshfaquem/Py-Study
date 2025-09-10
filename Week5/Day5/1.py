
# bulk_create() is a QuerySet method in Django.
# It allows you to insert multiple objects into the database
# Instead of looping and calling .save() on each object, you can update them in a single query.
# here one query used instead of saving them one by one.
# This makes inserts much faster and efficient, especially when adding large datasets.

# ✅ Syntax
# Model.objects.bulk_create([
#     Model(field1=value1, field2=value2, ...),
#     Model(field1=value3, field2=value4, ...),
#     ...
# ])

# ✅ Key Points
# Performance boost – fewer queries = faster execution.
# No signals – unlike .save(), bulk_create() does not trigger signals (post_save, etc.).
# Return value – returns a list of the created objects (with IDs filled in, depending on the DB backend).
# Batching – if inserting thousands of records, you can use the batch_size parameter:
# Employee.objects.bulk_create(employee_list, batch_size=1000)

# ✅ Analogy
# Think of .create() like buying items one by one at the store checkout.
# But .bulk_create() is like loading everything into the cart and paying once — much faster.