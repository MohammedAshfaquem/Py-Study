# ChatGPT said:
# In Django, a custom middleware is your own piece of code that sits between the request and the response and
# can process them before or after the view is called.


# it can  modify the request before it reaches the view
# it can modify the response before it is sent back to the browser.


# ✅ Real-life use cases of custom middleware
# Logging requests & responses.
# Blocking IP addresses.
# Adding custom headers.
# Measuring performance.
# Modifying request data before reaching the view.


# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Code before the view runs
#         print("Hello from middleware")

#         # Call the view
#         response = self.get_response(request)

#         # Code after the view runs
#         return response
