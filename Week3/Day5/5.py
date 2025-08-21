# ✅ Simple Definition:
# Denormalization is the opposite of normalization. It’s used to make data retrieval faster by reducing the number of joins.


# 🔑 Key Points About Denormalization
# 🔁 Adds Redundant Data
# Data is repeated intentionally across tables.

# 🔗 Reduces Complex Joins
# Queries become faster and simpler because data is stored in fewer tables.

# ⚡ Improves Read Performance
# Especially useful in systems with lots of reads and fewer writes (e.g., reporting systems).

# 🐢 May Slow Down Writes
# Since data is repeated, updating it in multiple places becomes harder and slower.





# | Feature         | Normalization              | Denormalization            |
# | --------------- | -------------------------- | -------------------------- |
# | Data Redundancy | Reduced / eliminated       | Intentionally added        |
# | Query Speed     | Slower (joins needed)      | Faster (fewer joins)       |
# | Data Integrity  | High (less duplication)    | Risk of inconsistency      |
# | Use Case        | OLTP (transaction systems) | OLAP (reporting/analytics) |
# | Write Speed     | Fast                       | Slower                     |
