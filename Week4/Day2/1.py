# 🧩 Full Function:
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.password = hash_password(user.password)
#             user.save()
#             messages.success(request, 'User registered successfully!')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})

# 🔍 Step-by-step Explanation:
# def register(request):
# Defines a view function named register.
# Takes the request object as input (sent by the user’s browser).
# This function will handle both GET and POST requests to the registration page.

# if request.method == 'POST':
# Checks if the form was submitted via POST method.
# If it’s a POST, the user has submitted the form (i.e., clicked the Register button).
# Otherwise, it’s likely a GET request (i.e., the user just opened the page).


# form = UserRegisterForm(request.POST)
# Creates a form instance (form) using the submitted POST data (request.POST).
# UserRegisterForm is your custom form class (linked to your users model).
# This binds the data entered by the user to the form for validation.

# if form.is_valid():
# Checks whether all required fields are filled and formatted correctly.
# Validates things like:
# Email format
# Required fields not left empty
# Field types match (e.g. age is an integer)

# user = form.save(commit=False)
# Converts form data into a user model object, but doesn’t save it to the database yet.
# commit=False lets you modify the object before saving, like hashing the password.

# user.password = hash_password(user.password)
# Replaces the plain-text password with a hashed version using your custom hash_password() function (probably using hashlib).
# This is important for security: we never store plain-text passwords.

# user.save()
# Now the user object is saved to the database.
# At this point, the user’s name, age, email, and hashed password are stored in your users table.
# messages.success(request, 'User registered successfully!')
# Sends a success message that can be displayed in the template.
# Example usage in your HTML:

# {% for message in messages %}
#     <p>{{ message }}</p>
# {% endfor %}

# else:
# If the request method isn't POST, that means the user just opened the registration page.
# So we need to send them a blank form to fill.

# form = UserRegisterForm()
# Creates an empty form instance to be rendered in the template.
# This shows input fields for name, age, email, password.
# return render(request, 'register.html', {'form': form})
# Renders the register.html template.
# Passes the form object to the template context, so you can display the form in HTML using {{ form.as_p }} or similar.

# ✅ Summary Diagram:
# Request Type	Action
# GET	Show empty registration form
# POST (form submitted)	Validate → Hash password → Save user → Show success message