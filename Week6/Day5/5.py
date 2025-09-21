# 🔄 Reusable Apps with DRF
# we create an app inside one project.
# Later, you can take that app folder and plug it into another project without rewriting the code.
# Key Points:
# Self-contained apps → keep models, serializers, views, urls, and tests inside one app folder.
# Pluggable design → example: users, auth, or blog app can be reused across projects.
# Best practice → avoid project-specific logic inside reusable apps; make them generic.

# 🔹 Monitoring & Logging API Requests (with Sentry)
# APIs  not only give correct responses but also be monitored to check errors, speed, and how clients are using them.
# Monitoring helps in debugging and improving reliability.

# 📌 Why it’s useful
# Detect errors quickly (e.g., API returning 500).
# Track slow API endpoints (performance bottlenecks).
# Get alerts when something breaks in production.
# Use Sentry for production monitoring.
# Helps in debugging, performance tracking, and error alerts.


Swagger/ReDoc 
# 👉 Useful for: automatically generating interactive API docs so developers can test and understand your APIs easily.
# Key Points:
# Swagger UI → provides a web-based interactive interface.
# ReDoc → clean, structured documentation, better for large APIs.
# DRF integration → use tools like drf-yasg or drf-spectacular to auto-generate docs from serializers & views.



# ⚡ DRF + Django Channels for Real-time APIs
# 👉 Useful for: building features that need live updates (chat, notifications, dashboards).
# 🔑 Key Points
# Django REST Framework (DRF) → handles normal HTTP APIs (request/response).
# Django Channels → adds WebSocket support for real-time communication.
# Together → you can build both REST APIs and real-time APIs in the same project.


# 📈 Building Scalable APIs
# 👉 Useful for: handling high traffic and making APIs faster, reliable, and efficient.

# 🔑 Key Points
# Caching 🗂️
# Stores frequently used data (e.g., popular API responses) in memory.
# Reduces database hits → faster responses.
# Example: use Redis or Django’s cache framework.

# Throttling ⏳
# Limits how many requests a user/client can make in a time period.
# Prevents abuse, spam, or DDoS attacks.
# Example: UserRateThrottle in DRF.

# Batching 📦
# Instead of multiple API calls, group them into one request.
# Saves network overhead and improves performance.
# Example: fetch multiple resources in a single API call.