# 🔁 What is a Transaction?
# A transaction is a sequence of one or more operations (usually database queries or updates)
# it treated as a single unit of work.
# Here all operations in the transaction succeed, or none do.it

# Example:
# Transferring money from one bank account to another:
# Debit $100 from Account A
# Credit $100 to Account B
# If either step fails, the whole transaction should be undone.




# | Property            | Description                                                                                                |
# | ------------------- | -------------------------------------------------------------------------------------------                |
# | **A** — Atomicity   | All operations in the transaction either complete or none do. No partial updates.                          |
# | **C** — Consistency | The database starts and ends in a consistent state (check it follow  all rules and constraints).           |
# | **I** — Isolation   | When many people use the database at the same time (like updating the same table), there could be conflicts|
# | **D** — Durability  | Once a transaction is committed, changes are permanent, even if there's a crash.                           |



# ⚠️ Common Problems without Proper ACID:
# Dirty Read: Reading uncommitted data from another transaction
# Non-repeatable Read: Getting different results when reading the same data in a single transaction
# Phantom Read: New rows appear during a transaction when data is queried again