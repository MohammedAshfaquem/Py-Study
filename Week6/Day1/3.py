# 🔹 JSON (JavaScript Object Notation)

# Lightweight text format.
# Easier to read for humans and machines.
# Mostly used in modern APIs.
# Default output of DRF.


# Example:
# {
#   "id": 1,
#   "title": "First Post",
#   "content": "Hello World"
# }


# 🔹 XML (eXtensible Markup Language)
# Older data format (used before JSON became popular).
# More verbose (lots of tags).
# Still used in some banking,legacy systems.

# Example:
# <Post>
#   <id>1</id>
#   <title>First Post</title>
#   <content>Hello World</content>
# </Post>

# ⚖️ Key Differences: JSON vs XML
# Feature	        JSON	                                                        XML
# Readability	    Easy (less code)	                                            Harder (more tags)
# Size	            Small (compact)	                                                Large (verbose)
# Data Type         Support	Supports numbers, strings, arrays, booleans	            Mostly text (needs parsing)
# Speed	            Faster to parse	                                                Slower
# Use Today	        REST APIs, Web apps, Mobile apps	                            Legacy APIs, SOAP, configs
# DRF Default	    ✅ Yes	                                                       ❌ Optional