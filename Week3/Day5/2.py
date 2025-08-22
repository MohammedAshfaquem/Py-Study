# ✅ Transaction Commands in SQL
# Transaction commands help manage database transactions.


# 🔹 1. BEGIN or START TRANSACTION
# Starts a new transaction.
# Use: Tells the database, “We are starting a group of operations that should be treated as a single unit.”
# Syntax:
# BEGIN;
# -- or
# START TRANSACTION;


# 🔹 2. COMMIT
# If all operations are successful, commit them to the database.
# Syntax:
# COMMIT;


# 🔹 3. ROLLBACK
# Use: If an error occurs, or something goes wrong, undo all changes.
# Syntax:
# ROLLBACK;

# 🔹 4. SAVEPOINT
# it is like checkpoint .so we can roll back to specific point instead of roll back whole transaction
# Use: Useful in complex transactions where you want partial undo.
# Syntax:
# SAVEPOINT savepoint_name;

# 🔹 5. ROLLBACK TO SAVEPOINT
# Undo changes only up to a specific savepoint, not the entire transaction.
# Use: Go back to a known good state in the middle of a transaction.
# Syntax:
# ROLLBACK TO SAVEPOINT savepoint_name;


# 🔹 6. RELEASE SAVEPOINT
# Removes a savepoint that you no longer need.
# Use: To clean up and free resources if you don’t need the savepoint anymore.
# Syntax:
# RELEASE SAVEPOINT savepoint_name;