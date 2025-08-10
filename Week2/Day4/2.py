# Cookies in Django
# Definition: Cookies store data on the client side (i.e., in the user's browser).
# They are key-value pairs that a server sends to the client, which are sent back to the server with every subsequent request.

# 🔹 Explanation of
# response.set_cookie('name', 'John')
# This line:
# Sets a cookie on the HTTP response.
# The cookie will have:
# Key: 'name'
# Value: 'John'
# The browser stores this cookie and sends it back to the server on future requests to the same domain.

# 🔸 When and where you use this:
# You call set_cookie() on an HttpResponse object in Django. Example:
# from django.http import HttpResponse

# def my_view(request):
#     response = HttpResponse("Cookie Set!")
#     response.set_cookie('name', 'John')  # ← setting the cookie
#     return response
# This will send a Set-Cookie header in the HTTP response, like:
# Set-Cookie: name=John
# Then the browser saves this cookie and includes it in future requests like:
# Cookie: name=John
# 🔹 Accessing a cookie (from the client):
# To get the cookie back in another view:
# def read_cookie(request):
#     name = request.COOKIES.get('name')
#     return HttpResponse(f"Hello {name}")
# 🔹 Optional parameters for set_cookie():
# You can customize cookie behavior with options like:
# response.set_cookie(
#     key='name',
#     value='John',
#     max_age=3600,           # Expires in 1 hour (in seconds)
#     expires=None,           # Specific datetime for expiry
#     path='/',               # URL path this cookie is valid for
#     domain='.example.com',  # Domain the cookie applies to
#     secure=True,            # Only send over HTTPS
#     httponly=True,          # Not accessible via JavaScript
#     samesite='Lax',         # CSRF protection
# )
# 🔹 Difference between Cookie and Session:
# Feature	Cookie	Session
# Storage	Client-side (browser)	Server-side
# Size Limit	~4KB	Much larger possible
# Security	Less secure	More secure (data not exposed)
# Persistence	Controlled by expiry settings	Can expire with browser/session