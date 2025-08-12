
# 🔹 What is a QuerySet?
# A QuerySet is a collection of  rows in DB  that returned by Django ORM .
# You use it to read, filter, order, update, or delete data.

# 🔸 Basic Queries
# all()
# Returns all records from the table:
# Book.objects.all()

# filter()
# Filters the records using conditions:
# Book.objects.filter(author='Alice')
# Book.objects.filter(published_year__gte=2020)
# get()

# Fetches a single object:
# Book.objects.get(id=1)
# Raises DoesNotExist or MultipleObjectsReturned if no or multiple results.
# first() / last()
# Returns the first or last object from a queryset:
# Book.objects.filter(author='Alice').first()


# 🔸 Field Lookups (Filters)
# Django supports a rich syntax to filter data:
# Lookup	Description	Example
# exact	Exact match	filter(title__exact='Django')
# iexact	Case-insensitive exact match	filter(title__iexact='django')
# contains	Substring match	filter(title__contains='Django')
# icontains	Case-insensitive contains	filter(title__icontains='django')
# in	Value in a list	filter(id__in=[1,2,3])
# gt, gte	Greater than / greater or equal	filter(year__gt=2020)
# lt, lte	Less than / less or equal	filter(year__lte=2023)
# startswith	Starts with	filter(title__startswith='Intro')
# istartswith	Case-insensitive startswith	filter(title__istartswith='intro')
# endswith	Ends with	filter(title__endswith='Guide')
# range	Between two values	filter(year__range=(2010, 2020))
# isnull	Is NULL (or not)	filter(summary__isnull=True)



# 🔸 Ordering & Limiting
# order_by()
# Sort results:
# Book.objects.order_by('title')      # ASC
# Book.objects.order_by('-published_year')  # DESC
# Limiting



# Python slicing applies directly:
# Book.objects.all()[:5]      # First 5 books
# Book.objects.order_by('title')[10:20]  # Pagination: items 11–20
# 🔸 Updating Records
# Book.objects.filter(author='Alice').update(is_best_seller=True)
# 🔸 Deleting Records
# Book.objects.filter(published_year__lt=2000).delete()
# 🔸 Chaining Queries
# QuerySets can be chained:
# Book.objects.filter(author='Alice').filter(published_year__gte=2020)

# This is the same as:
# Book.objects.filter(author='Alice', published_year__gte=2020)
# 🔸 Aggregate & Annotation
# aggregate() – summary values (like SQL SUM, AVG, etc.)
# from django.db.models import Avg, Max
# Book.objects.aggregate(Avg('published_year'))
# annotate() – adds computed fields to each object.
# from django.db.models import Count
# Author.objects.annotate(book_count=Count('book'))
# 🔸 Raw SQL (if needed)

# You can also run raw SQL if needed:
# Book.objects.raw('SELECT * FROM app_book WHERE author = %s', ['Alice'])     raw sql
# Summary
# Operation	Code Example
# All         records	Book.objects.all()
# Filter	    Book.objects.filter(year__gte=2020)
# Get         single	Book.objects.get(id=1)
# Update	    Book.objects.filter(id=1).update(title=...)
# Delete	    Book.objects.filter(id=1).delete()
# Order	    Book.objects.order_by('-year')
# Limit	    Book.objects.all()[:5]



# 🔍 What is a Query in Django?
# A query is a request for data from the database.
# In Django, queries are written using Python code via the ORM, and they’re converted into SQL behind the scenes.

# ✅ Example:
# 1. Query (asking for data):
# Book.objects.filter(author='Alice')
# This is a query:
# “Get me all books where the author is Alice.”

# 2. QuerySet (the result):
# qs = Book.objects.filter(author='Alice')
# qs is a QuerySet — a collection of book objects matching the query.

# This gets converted to SQL like:
# SELECT * FROM books WHERE author = 'Alice';
# 🔸 Behind the Scenes
# Django ORM turns Python code into SQL queries.
# You can even view the actual query:
# qs = Book.objects.filter(author='Alice')
# print(qs.query)
# Output (SQL):
# SELECT * FROM "app_book" WHERE "app_book"."author" = 'Alice';


# 🧠 Summary
# Term	     Meaning
# Query	     A request for data (what you ask the DB to do)
# QuerySet	 The result of a query (like a list of objects)
# SQL	     The actual database language Django uses under the hood