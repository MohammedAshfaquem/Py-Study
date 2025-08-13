# sessions allow you to store and retrieve data on a per-user basis while the user interacts with your web application.
# This is useful for things like keeping users logged in,
# storing shopping cart contents,
# tracking user preferences.

# 🔹 Explanation of request.session['user'] = 'John':
# This line of code:
# request.session['user'] = 'John'
# means:
# You're storing data ('John') into the session dictionary under the key 'user'.
# The request.session object works like a dictionary, but instead of being stored in memory (like a normal Python dict),
# it stores data on the server side and tracks it using a session ID saved in the user's browser as a cookie.
# So, this line is saying:

# “Save the value 'John' as the 'user' in the session data for this particular user.”

# 🔹 What happens behind the scenes:
# Django checks if the user already has a session ID (via a cookie).
# If not, Django creates a new session and assigns an ID.
# The session ID is sent to the user as a cookie (sessionid).
# The value 'John' is saved in the server-side session store (e.g., database, cache, or file depending on settings).
# On the next request, Django reads the sessionid cookie, finds the corresponding session, and restores the session data including 'user': 'John'.

# 🔹 Accessing the session data later
# username = request.session.get('user')
# print(username)  # Output: John
# 🔹 Session configuration in Django settings:
# By default, Django uses the database-backed session engine. This is defined in settings.py:
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Other options include:
# 'cache' – Store sessions in cache.
# 'file' – Store sessions in files.
# 'signed_cookies' – Store session data in cookies (encrypted).