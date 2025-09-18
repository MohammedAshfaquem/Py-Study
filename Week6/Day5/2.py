# 🔍 Title: Filtering, Search & Pagination
# APIs  return lots of data → we need filtering, search, and pagination to keep responses efficient and useful.

# 1️⃣ Filtering (filter_backends)
# 👉 Useful for exact field-based queries using(DjangoFilterBackend).
# Example: /api/books/?author=John

# 2️⃣ Search (SearchFilter)
# 👉 Useful for: keyword-based flexible search.
# Example: /api/books/?search=Python

# 3️⃣ Ordering (OrderingFilter)
# 👉 Useful for: sorting results (asc/desc).
# Example: /api/books/?ordering=title or /api/books/?ordering=-title

# 4️⃣ Pagination Classes
# 👉 Useful for: breaking large data into smaller pages.
# PageNumberPagination → simple page numbers.
# LimitOffsetPagination → control count & start position.
# CursorPagination →  instead of page numbers Use encoded cursor



