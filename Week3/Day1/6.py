🔑 Keys in SQL:
Keys are used to identify rows uniquely in a table and link tables together.


| Key Type      | Description                                                      | Example                                                     |
| --------------| ---------------------------------------------------------------- | ----------------------------------------------------------- |
| Primary Key   | Uniquely identifies each row in a table.                         | `id` column in a `students` table.                          |
| Foreign Key   | Links one table to another (creates a relationship).             | `student_id` in `marks` table refers to `id` in `students`. |
| Unique Key    | Ensures all values in a column are unique.                       | Email address must be unique.                               |
| Composite Key | A combination of two or more columns to uniquely identify a row. | `order_id + product_id` in order details.                   |
| Candidate Key | Columns that can be a primary key (but only one is chosen).      | `id`, `email`, `username`.                                  |
| Alternate Key | Candidate keys not selected as the primary key.                  | `email` or `username` if `id` is primary.                   |


📏 Constraints in SQL:
Constraints are rules applied to columns to enforce data integrity and validity.

| **Constraint**  | **Purpose**                                      | **Example**                                        |
| --------------- | ------------------------------------------------ | -------------------------------------------------- |
| **NOT NULL**    | Prevents empty (null) values in a column         | `name VARCHAR(50) NOT NULL`                        |
| **UNIQUE**      | Ensures all values in a column are different     | `email VARCHAR(100) UNIQUE`                        |
| **PRIMARY KEY** | Combines `UNIQUE + NOT NULL`                     | `id INT PRIMARY KEY`                               |
| **FOREIGN KEY** | Ensures a value matches a value in another table | `FOREIGN KEY (student_id) REFERENCES students(id)` |
| **CHECK**       | Ensures values meet a specific condition         | `age INT CHECK (age >= 18)`                        |
| **DEFAULT**     | Sets a default value if none is provided         | `status VARCHAR(10) DEFAULT 'active'`              |


✅ In Simple Words: 
Keys help identify and connect data.
Constraints help protect and validate your data.