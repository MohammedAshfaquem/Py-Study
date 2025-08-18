    # DATA TYPES

# 🔹 String / Character Types
# CHAR(n) → Fixed-length string (e.g., CHAR(5) always stores 5 characters).
# VARCHAR(n) → Variable-length string, up to n characters (commonly used).
# TEXT → Large text data (no fixed limit, depends on DB system).
# NVARCHAR(n) → Like VARCHAR but supports Unicode characters.

# 🔹 Numeric Types
# INT / INTEGER → Whole numbers (e.g., 10, -45).4 bytes  salary,
# BIGINT → Large integers. 8 Bytes,population conts 
# SMALLINT / TINYINT → Small integers with less storage. 2 bytes age 
# DECIMAL(p, s) or NUMERIC(p, s) → Fixed-point numbers (e.g., DECIMAL(5,2) → 999.99).p=Precison ,Scale 
# FLOAT / REAL / DOUBLE → Approximate decimal numbers (good for scientific calculations).
# 4 to 8/  4   /  8   
# 7-15     7      15-16  

# 🔹 Date and Time Types
# DATE → Stores only date (YYYY-MM-DD).
# TIME → Stores only time (HH:MM:SS).
# YEAR → Only year.
# DATETIME → Date and time together.
# TIMESTAMP → Date and time with automatic update capability in some DBs.

# 🔹 Boolean Type
# BOOLEAN or BOOL → TRUE or FALSE (internally often stored as 1 or 0).

# 🔹 Binary / Misc Types
# BLOB → Binary Large Object (images, files, etc.).
# JSON → Stores JSON data (supported in MySQL, PostgreSQL).
# UUID → Universally unique identifier.