✅ What is Normalization?
Normalization is the process of organizing data in a database to reduce redundancy (repetition) and improve data integrity.

🔑 Key Points:
🧹 Removes Duplicate Data
Same data isn’t stored in multiple places.
🔗 Creates Relationships Using Foreign Keys
Large tables are broken into smaller related tables.
🛡️ Improves Data Integrity
Ensures that changes in one place update everywhere (no mismatch).
📈 Improves Efficiency
Reduces the amount of space used and improves query performance (in many cases).



📘 Types of Normalization (Normal Forms)


🔹 1. First Normal Form (1NF)
Rule:
Each column should have atomic (indivisible) values.

Example (Before 1NF):
Student	Subjects
Raj	Math, Science

After 1NF:
Student	Subject
Raj	Math
Raj	Science


🔹 2. Second Normal Form (2NF)
Rule:
Must be in 1NF
NO Partial Dependency
All non-key columns must depend on the entire primary key, not part of it.


🔹 3. Third Normal Form (3NF)
Rule:
Must be in 2NF
No transitive dependency (non-key column depending on another non-key column).
Example:
StudentID	Name	DeptID	DeptName
Here, DeptName depends on DeptID, which is not the primary key → violates 3NF.
Fix: Move Dept info to a separate table.

4. Boyce-Codd Normal Form (BCNF)
Rule:
Stricter version of 3NF.
Every determinant must be a candidate key.
Used when 3NF still allows some anomalies due to composite or overlapping candidate keys.