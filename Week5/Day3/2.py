# 🔹 What is Meta in Django?
# It is an inner class inside your model.
# Used to configure metadata (extra options) about the model.
# It does not define fields, but controls how the model behaves with the database and admin.



# | Option                | What it does                                                     | Example                                                             |
# | --------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------- |
# | `db_table`            | Sets custom table name in DB (default is `appname_modelname`)    | `db_table = "my_users"`                                             |
# | `ordering`            | Default ordering of querysets                                    | `ordering = ['name']` or `['-age']`                                 |
# | `verbose_name`        | Singular name shown in admin                                     | `"User Profile"`                                                    |
# | `verbose_name_plural` | Plural name shown in admin                                       | `"User Profiles"`                                                   |
# | `unique_together`     | Ensure combination of fields is unique                           | `unique_together = ('name', 'age')`                                 |
# | `constraints`         | Add database-level constraints                                   | `[models.CheckConstraint(check=Q(age__gte=18), name="age_gte_18")]` |
# | `abstract`            | Makes model abstract (no DB table)                               | `abstract = True`                                                   |
# | `managed`             | If `False`, Django won’t create/drop table (used for legacy DBs) | `managed = False`                                                   |

# 🔹 In short:
# Meta = model configuration hub.
# It customizes DB behavior, admin display, constraints, ordering, etc.
# It’s optional → if you don’t define it, Django uses defaults.
Test