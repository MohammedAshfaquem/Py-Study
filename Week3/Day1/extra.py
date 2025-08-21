# UPDATE users SET age = CASE
# WHEN id = 1 THEN 20
# WHEN id = 5 THEN 23
# WHEN id = 2 THEN 22
# END
# WHERE id IN(1,5,2);
# SELECT * FROM users

# UPdate Multple data same time


# ALTER TABLE table_name
# ALTER COLUMN column_name TYPE new_data_type;
# update data type of column


# ALTER TABLE old_table_name
# RENAME TO new_table_name;
# Rename Table