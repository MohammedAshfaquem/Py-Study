# What is Django ORM?
# ORM = Object Relational Mapping
# It lets you work with your database using Python classes and methods instead of raw SQL
# You define models (Python classes), and Django creates corresponding database tables.
# You query and manipulate data using Python code.


# 3. Create Records
# You can create a new record (row) like this:
# book = Book(title='Django Basics', author='Alice', published_year=2023)
# book.save()
# Or shortcut:
# book = Book.objects.create(title='Django Basics', author='Alice', published_year=2023)

# 4. Read / Query Records
# Get all books:
# books = Book.objects.all()
# Filter books by author:
# books = Book.objects.filter(author='Alice')
# Get one book (raises error if not found):
# book = Book.objects.get(id=1)
# Get or None (safer):
# book = Book.objects.filter(id=1).first()
# Order results:
# books = Book.objects.order_by('published_year')  # ascending
# books = Book.objects.order_by('-published_year') # descending

# 5. Update Records
# book = Book.objects.get(id=1)
# book.title = 'Updated Title'
# book.save()
# Or bulk update:
# Book.objects.filter(author='Alice').update(is_best_seller=True)\
    
# 6. Delete Records
# book = Book.objects.get(id=1)
# book.delete()
# Or bulk delete:
# Book.objects.filter(published_year__lt=2000).delete()

# 7. Common Query Lookups
# Exact match: filter(author='Alice')
# Case-insensitive: filter(author__iexact='alice')
# Contains substring: filter(title__contains='Django')
# Greater than: filter(published_year__gt=2010)
# Less or equal: filter(published_year__lte=2023)

# Summary
# Operation	Django ORM Code
# Create	    Book.objects.create(...)
# Read all	Book.objects.all()
# Filter	    Book.objects.filter(...)
# Get single	Book.objects.get(id=1)
# Update	    obj.save() or Book.objects.update(...)
# Delete	    obj.delete() or Book.objects.filter(...).delete()


# Model = Table:
# Django converts this model into an SQL table when you run makemigrations and migrate.