# 1. redirect()
# 📌 Definition
# A shortcut function in Django .
# it used to redirect the to another URL.
# It returns an HttpResponseRedirect object.

# 📌 How it works
# You can redirect using:
# A URL pattern name
# A model object
# A direct URL string

# 📌 Example
# from django.shortcuts import redirect

# def my_view(request):
#     # Redirect to a URL name
#     return redirect("home")

# def another_view(request):
#     # Redirect to a specific URL
#     return redirect("/success/")

# def profile_view(request, user_id):
#     # Redirect to another view with arguments
#     return redirect("profile", user_id=user_id)


# 2. reverse_lazy()
# 📌 Definition
# A lazy version of reverse().
# which converts a URL pattern name into an actual URL string.
# Called lazy because it doesn’t evaluate the URL Evaluates only when accessed.
# Very useful in class-based views (where URLs might not be loaded at import time).
# 👉 Without reverse_lazy, you might get import errors because Django tries to resolve URLs before the URLconf is ready.

# | Feature | `redirect()`                                | `reverse_lazy()`                          |
# | ------- | ------------------------------------------- | ----------------------------------------- |
# | Purpose | Immediately redirects user to another URL   | Lazily resolves a URL into string         |
# | Returns | `HttpResponseRedirect` object               | String (URL path)                         |
# | Usage   | Inside views (function-based / class-based) | Usually in class attributes (CBVs, forms) |
# | Timing  | Evaluates immediately                       | Evaluates only when accessed              |
