# 🔍 What it does:
# It hashes the user's password before saving it to the database.
# 🧠 Why is this important?
# If you don’t hash the password, it will be stored in plain text in your database — which is:
# ❌ A huge security risk
# ❌ Easy for anyone with DB access to see user passwords
# ❌ Bad practice — never store raw passwords


✅ What does hash_password() do?
It’s usually something like this (with hashlib):
    
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

So:
user.password = hash_password(user.password)

will replace something like:
"hello123"
with:
"fcea920f7412b5da7be0cf42b8c93759"  ← (SHA-256 hash)

🔒 Why do we hash passwords?
Reason	Benefit
🛡️ Security	If the DB is hacked, raw passwords aren’t exposed
🔐 Privacy	Even admins/devs can’t read user passwords
🔁 Best Practice	Follows industry standards
✅ Summary

This line:

user.password = hash_password(user.password)


replaces the raw password with a hashed version before saving to the database, so it’s safe and secure.