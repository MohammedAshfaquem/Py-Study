# ✅ Django Form – Definition:
# A Django Form is a Python class used to create and handle HTML forms.
# It simplifies form creation, input validation, and error handling.


# 📌 Key Points about Django Forms:
# 🔹 1. Two Types of Forms:
# forms.Form – For creating custom forms not directly linked to models.
# forms.ModelForm – For creating forms directly from models (auto-generates fields).

# 🔹 2. Purpose of Django Forms:
# Render HTML form elements (textboxes, checkboxes, etc.)
# Receive and process user input (GET or POST)
# Validate input (type checks, length checks, etc.)
# Display form errors when validation fails
# Secure against CSRF attacks

# 🔹 3. Common Field Types:
# forms.CharField()
# forms.EmailField()
# forms.IntegerField()
# forms.BooleanField()
# forms.DateField()
# forms.ChoiceField(choices=[...])

# 🔹 4. Built-in Validators:
# Django provides validators like:
# from django.core.validators import MinLengthValidator, MaxValueValidator
# These help enforce rules like:
# Minimum length
# Maximum value
# Regex matching
# Required fields (default behavior)


# example:username = forms.CharField(max_length=20, validators=[MinLengthValidator(5)])
# password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8)])


# 🧠 Summary:
# Feature	Description
# Easy Form Creation	Define fields using forms.Form or ModelForm
# Built-in Security	CSRF protection, field validation
# Clean Data Access	form.cleaned_data['field']
# Error Handling	Auto-handles invalid input
# Integration	Works with models, views, and templates


# creation:
# views.py
# from django.shortcuts import render
# from .forms import Register

# def register(request):
#     if request.method == 'POST':
#         form = Register(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             age = form.cleaned_data['age']
#             return render(request,'home.html',{'name':name,'email':email,'age':age})
#     else:
#         form =Register()
#     return render(request,'register.html',{'form':form})
# # Create your views here.


# forms.py:
# from django import forms
# from django.core.validators import MaxLengthValidator,MaxValueValidator,MinValueValidator,MinLengthValidator
# class Register(forms.Form):
#     name = forms.CharField(max_length=100,validators=[MinLengthValidator(2),MaxLengthValidator(10)])
#     email = forms.EmailField(validators=[MinLengthValidator(5),MaxLengthValidator(50)])
#     age = forms.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])



# ✅ 1. forms.Form
# 🔹 What is it?
# A plain Django form.
# You define each field manually.
# It is not linked to any model.

# 🔹 When to use?
# When the form is not directly related to a database model.
# For example: contact forms, search forms, custom filters, etc.

# 🔹 Example:
# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
# You control everything yourself: validation, saving, etc.

# ✅ 2. forms.ModelForm
# 🔹 What is it?
# A Django form linked to a model.
# It automatically generates form fields based on the model.

# 🔹 When to use?
# When the form is used to create or update model instances.

# Less code to write, built-in save functionality.

# 🔹 Example:
# from django import forms
# from .models import Student

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'age']
# You just define which model and fields — Django handles the rest.

# 🆚 Summary Table
# Feature	             forms.Form	                              forms.ModelForm
# Linked to Model	     ❌ No	                                ✅ Yes
# FieldsDefined Manually ✅ Yes	                                ❌ Auto-generated from model
# Use Case	             Custom forms, filters, etc.	          Create/update model objects
# Needs .save()          Method	❌ You handle saving manually	✅ Comes with .save() method
# Flexibility	         ✅ Very flexible	                    ⚠️ Less flexible, but easier for models

    
