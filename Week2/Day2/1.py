# 🧩 Django Templates – Explained
# ✅ Definition
# Templates are HTML files that use Django Template Language (DTL) to display dynamic content like user names, posts, or database data.

# 💡 Think of templates as the "presentation layer"—what users see on the website.

# Example:
# <!-- home.html -->
# <h1>Welcome, {{ user.username }}!</h1>
# Here, {{ user.username }} is a Django template variable that will be replaced by real data at runtime.

# 🏗️ Template Inheritance
# Allows you to create a base layout (like a skeleton) and then reuse it across multiple pages.

# 🔹 Example:
# base.html:
# <!-- templates/base.html -->
# <!DOCTYPE html>
# <html>
# <head>
#     <title>My Site</title>
# </head>
# <body>
#     <header>Header content</header>

#     {% block content %}
#     <!-- Child templates will inject content here -->
#     {% endblock %}

#     <footer>Footer content</footer>
# </body>
# </html>
# home.html:
# <!-- templates/home.html -->
# {% extends "base.html" %}

# {% block content %}
# <h1>This is the homepage!</h1>
# {% endblock %}
# ✅ This allows you to:

# Keep your layout consistent

# Avoid repeating HTML in every file

# Follow DRY (Don't Repeat Yourself) principle

# 🧱 Block Content
# Used inside templates to mark replaceable sections.

# Syntax:
# {% block content %}
#     <!-- dynamic content here -->
# {% endblock %}
# Why it's useful:
# Makes your templates modular and easier to manage

# Each child template can change only specific parts without touching the whole layout

# ✅ Summary Table
# Feature	Purpose
# Templates	HTML + Django code to show dynamic data
# Template Inheritance	Reuse base layout across many pages
# {% block content %}	Define sections that child templates can override
# {% extends 'base.html' %}	Inherit layout from a parent/base template