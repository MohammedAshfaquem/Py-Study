# 🔹 What are Django Signals?
# In Django, signals are a way for different parts of our application to communicate with each other when certain events happen.
# it is mainy used for side effect handling like notification ,send email,logging etc...

# 👉 Think of signals like a notification system:
# Sender → triggers an event (like "a user is saved").
# Receiver → listens for that event and runs some code in response.

# 🔹 When are signals useful?
# When you want to do something automatically after a certain action.

# Example:
# After a new user is created → automatically create a profile.
# After an order is placed → send a confirmation email.
# After a blog post is saved → update a search index.

# 🔹 Built-in Django Signals
# Some common signals Django provides:
# pre_save → before a model is saved.
# post_save → after a model is saved.
# pre_delete → before a model is deleted.
# post_delete → after a model is deleted.
# m2m_changed → when a many-to-many field is changed.
# request_started / request_finished → when a request starts/ends.

# 🔹 Example: Create Profile after User is created
# # models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)

# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile

# # When a User is created, automatically create Profile
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# # When User is saved, also save the Profile
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# # apps.py (connect signals when app loads)
# from django.apps import AppConfig

# class MyAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'

#     def ready(self):
#         import myapp.signals

# 🔹 How it works here:
# A new User is created.
# post_save signal is triggered.
# Our create_user_profile function runs → creates Profile.
# Next save_user_profile ensures the profile is saved too.

# 🔹 Advantages of Signals
# ✅ Decouples logic → the User model doesn’t need to know about Profile.
# ✅ Makes code reusable.
# ✅ Keeps code cleaner (no need to repeat logic everywhere).

# 🔹 When NOT to use signals
# Don’t overuse signals for core logic (it can become hidden and hard to track).
# Use them for side-effects like sending emails, logging, notifications, etc.

# ⚡ In short:
# Signals = “Hey, something just happened!”
# Receivers = “Cool, let me react to it automatically.”

# just presave eg
# from django.db.models.signals import pre_save

# @receiver(pre_save, sender=Student)
# def uppercase_name(sender, instance, **kwargs):
#     instance.name = instance.name.upper()  # make name uppercase before saving
