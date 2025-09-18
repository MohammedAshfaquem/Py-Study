# ⚡ Title: Concurrency Handling
# When multiple users hit the API at the same time → race conditions can happen (e.g., two people buying the last item).
# to keep data consistent We need safe techniques 

# 1️⃣ Atomic Operations
# 👉 Useful for: making sure multiple DB actions happen as one unit.
# If one fails → all roll back.
# Prevents partial/dirty updates.

# Example:
# from django.db import transaction

# @transaction.atomic
# def create_order(request):
#     # deduct stock & create order in a single transaction
#     product = Product.objects.select_for_update().get(id=1)
#     if product.stock > 0:
#         product.stock -= 1
#         product.save()
#         Order.objects.create(product=product, user=request.user)


# ✅ Ensures stock + order update happen together.

# 2️⃣ Locking Strategies
# 👉 Useful for: avoiding race conditions when many users try to update the same row.
# Optimistic Locking → assume no conflict, check version/timestamp before saving.
# Pessimistic Locking → lock the row until transaction finishes.

# Example (Pessimistic Locking in Django):
# product = Product.objects.select_for_update().get(id=1)


# Locks that product row → no one else can change it until transaction ends.

# 3️⃣ Race Conditions Example
# User A & User B both try to buy the last book (stock=1).
# Without locking → both see stock=1 → both orders succeed → stock=-1 ❌.
# With atomic + locking → only one order goes through → stock=0 ✅