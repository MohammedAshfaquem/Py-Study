# | **Clause**    | **Purpose**                                 | **Example**                                                         |
# | ------------- | ------------------------------------------- | ------------------------------------------------------------------- |
# | `SELECT`      | Retrieve data from a table                  | `SELECT * FROM users;`                                              |
# | `FROM`        | Specifies the table to retrieve data from   | `SELECT name FROM users;`                                           |
# | `WHERE`       | Filters rows based on a condition           | `SELECT * FROM users WHERE age > 25;`                               |
# | `ORDER BY`    | Sorts the result set by one or more columns | `SELECT * FROM users ORDER BY name;`                                |
# | `GROUP BY`    | Groups rows that have the same values       | `SELECT age, COUNT(*) FROM users GROUP BY age;`                     |
# | `HAVING`      | Filters groups (used with `GROUP BY`)       | `SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 2;` |
# | `INSERT INTO` | Adds new rows to a table                    | `INSERT INTO users (name) VALUES ('Alice');`                        |
# | `UPDATE`      | Modifies existing data in a table           | `UPDATE users SET name = 'Bob' WHERE id = 1;`                       |
# | `DELETE`      | Deletes rows from a table                   | `DELETE FROM users WHERE id = 2;`                                   |
# | `LIMIT`       | Limits number of rows returned              | `SELECT * FROM users LIMIT 5;`                                      |
