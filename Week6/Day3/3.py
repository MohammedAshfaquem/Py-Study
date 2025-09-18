# 🔹 API Versioning in DRF
# 👉 APIs keep changing/evolve  over time. Sometimes we need multiple versions (v1, v2).
# so that old clients can still use the old version while new clients use the updated one.
# DRF provides different strategies for versioning.

# ✅ 1. Namespace Versioning
# here we create separate URL namespaces for each version.
# Clients call the version they need.

# Example (urls.py)
# from django.urls import path, include

# urlpatterns = [
#     path('api/v1/', include(('app.urls', 'app'), namespace='v1')),
#     path('api/v2/', include(('app.urls_v2', 'app'), namespace='v2')),
# ]


# 👉 Endpoints:
# /api/v1/books/ → old version
# /api/v2/books/ → new version

# 📌 Easy to use, clear for clients.

# ✅ 2. Accept Header Versioning
# Version info comes from HTTP header instead of URL.
# the client does not see version details in the URL
# Cleaner URLs, but client must send header.

# Example Request:
# GET /api/books/
# Accept: application/json; version=2.0


# 👉 DRF reads version from header and routes to correct view.
# 📌 URL stays the same (/api/books/), only header changes.

# ⚖️ Comparison
# Feature	         Namespace Versioning 🌐	        xAccept Header Versioning 📩
# Where is version?	 In URL (/api/v1/)	                In header (Accept: … version=2)
# Client visibility	 Very clear	                        Hidden (needs correct header)
# URL look	         Different                          per version	Same URL, flexible handling
# Best for	         Public APIs	                    Internal / advanced clients