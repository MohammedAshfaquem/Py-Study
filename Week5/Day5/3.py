# 1. AbstractUser
# A ready-made user model provided by Django.
# Inherits from AbstractBaseUser + PermissionsMixin.
# Already includes common fields like:
# username
# first_name
# last_name
# email
# is_staff
# is_active
# is_superuser
# Best when you just want to extend the default user model (e.g., add extra fields like phone_number, profile_pic).
# You don’t have to redefine authentication logic, forms, or managers.
# ✅ Use when: You want the default Django user functionality but with extra fields.


# To check Fields = print([f.name for f in Test._meta.get_fields()])


# 2. AbstractBaseUser
# A bare-bones user model.
# Provides only:
# password
# last_login
# authentication-related methods (set_password(), check_password()).
# Does not include username, email, is_staff, etc.
# You must define fields yourself (like username or email) and tell Django how to authenticate (via USERNAME_FIELD, REQUIRED_FIELDS).
# Requires writing your own UserManager (e.g., create_user, create_superuser).
# ✅ Use when: You want full control over the user model (e.g., login by email only, phone-only authentication).



# | Feature            | AbstractUser ✅              | AbstractBaseUser ⚡                                |
# | ------------------ | --------------------------- | ---------------------------------------------------- |
# | Predefined fields  | Yes (username, email, etc.) | No (only password, last\_login)                      |
# | Permissions system | Already included            | Must add manually (using PermissionsMixin if needed) |
# | Ease of use        | Easy (extend + go)          | Harder (define everything)                           |
# | Flexibility        | Limited                     | Full control                                         |
# | When to use        | Add extra fields only       | Completely custom authentication                     |
