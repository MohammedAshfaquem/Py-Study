# 🔑 Title: Third-party Auth (OAuth2, JWT)
# Sometimes, instead of handling usernames/passwords ourselves, we can :

# 1️⃣ JWT Authentication (JSON Web Token)
# tokens for secure stateless login.
# After login → server returns a JWT (looks like xxxxx.yyyyy.zzzzz).
# Client must send this token with each request:
# no sessions needed.

# Authorization: Bearer <your_jwt_token>

# In DRF → it commonly done with django-rest-framework-simplejwt.


# 2️⃣ OAuth2 (Google, Facebook, etc.)
# it allow users to sign in with third-party providers (google,facebook,github,etc...)
# Example: “Login with Google” button.

# Flow:
# User clicks Google login → redirected to Google.
# Google authenticates user → returns token to your API.
# Your API verifies token → create local user.

# 👉 Tools:
# django-allauth → handles social logins.
# dj-rest-auth → integrates with DRF for APIs.

# ⚖️ Why Important?
# JWT → secure, stateless, easy for mobile apps & SPAs.
# OAuth2 → better user experience (no new password needed).

# Both are industry-standard for scalable, modern APIs.

# 📝 Key Points
# JWT = self-contained token → fast, no DB lookup each time.
# OAuth2 = delegate authentication to trusted providers (Google, FB).
# DRF doesn’t ship with them → use packages (simplejwt, dj-rest-auth, allauth).
# Must be combined with HTTPS for security.