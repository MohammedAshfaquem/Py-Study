# 🔑 Title: Complex Authentication Workflows
# In real apps, just login/signup isn’t enough.
# We also need extra authentication steps like password resets and email verification to make accounts secure and reliable.


# 1️⃣ Password Reset
# it Allows a user to set a new password if they forget the old one.

# Typically done in two steps:
# requests reset → API sends an email with a reset token/link.
# clicks link    → API verifies token → lets them set a new password.

# 👉 Example (pseudo-steps):

# POST /api/password-reset/        # request reset, send email
# POST /api/password-reset-confirm/  # set new password

# 2️⃣ Email Verification
# Ensures that the user’s email is real and accessible.

# When a new account is created:
# Send an activation email with a verification link.
# User clicks → account marked as verified.
# Prevents fake or spam accounts.

# 👉 Example (pseudo-steps):

# POST /api/register/              # user signs up
# EMAIL: link → /api/verify-email/<token>/

# ⚖️ Why Important?
# Security → only real users can access accounts.
# Trust → reduces spam accounts, ensures communication works.
# Recovery → users can get back into their account if they forget credentials.

# 📝 Key Points
# Password reset uses tokens so only the real user can change the password.
# Email verification ensures the account belongs to a valid email address.
# Both are part of production-ready authentication workflows.
# DRF doesn’t give this out of the box → usually done with libraries like dj-rest-auth, django-allauth, or custom logic.