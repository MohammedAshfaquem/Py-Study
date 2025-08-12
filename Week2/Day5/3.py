# HTTP Methods in Django
# Django handles HTTP methods to let you interact with resources (like web pages, forms, APIs). The most common methods are:

# 1. GET
# Purpose: Retrieve data or render pages.
# Usage: When you want to fetch or display data without changing anything on the server.
# Access in Django: request.GET
# Example:
# def view_item(request):
#     item_id = request.GET.get('id')
#     # fetch item by id
#     return render(request, 'item.html', {'item': item})
# 2. POST
# Purpose: Send data to the server, usually to create or update resources.
# Usage: Form submissions, sending user input.
# Access in Django: request.POST
# Example:
# def submit_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         # process form data
#         return redirect('success')
#     return render(request, 'form.html')
# 3. PUT
# Purpose: Update an existing resource completely.
# Usage: Mostly in APIs; less common in standard Django views.
# Access in Django: request.body (requires parsing JSON or data manually)
# Example: Usually handled in Django REST Framework.
# 4. DELETE
# Purpose: Delete a resource.
# Usage: APIs or specific actions to remove data.
# Access in Django: Similar to PUT, usually requires manual handling.
# How Django Views Handle Methods
# You can check the method inside a view using:
# def my_view(request):
#     if request.method == 'GET':
#         # handle GET request
#     elif request.method == 'POST':
#         # handle POST request
#     # other methods...
# Or use class-based views to handle HTTP methods by defining functions like get(), post(), put(), delete().

# Summary:
# HTTP Method	Purpose	Django Access	Typical Use Case
# GET	        Retrieve data	        request.GET	Display pages, get info
# POST	        Submit data	            request.POST	Form submissions, create
# PUT	        Update data (API)	    request.body	REST API updates
# DELETE	    Delete data (API)	    request.body	REST API deletions