# Concurrency control:
# it is a techniques used to ensure that multiple transactions can be executed simultaneously
# without causing data inconsistency,conflicts, or errors.
# it allow users  to interact with the data in th DB at the same time.
# it allow users to handle or change data simulteniosly without affect  the data .


# Techniques of Concurrency Control:
    
# 1. Locking (ലോക്കിംഗ്):
# Exclusive Lock (X-lock): Prevents others from reading or writing the data until the transaction finishes.
# Shared Lock (S-lock): Allows multiple users to read the data but not modify it at the same time.


# How Locks Work:
# A transaction requests a lock.
# If another transaction holds a conflicting lock, the requesting transaction has to wait.
# Once the transaction is done, it releases the lock, and others can proceed.



# 2. Timestamp Ordering (ടൈംസ്റ്റാംപ്പ് ഓർഡറിങ്):
# Each transaction gets a timestamp.
# Transactions are executed in the order of their timestamps.


# 3. Optimistic Concurrency Control (ഓപ്റ്റിമിസ്റ്റിക് സമകാലിക നിയന്ത്രണം):
# No locks initially — transactions proceed under the assumption that no conflicts will occur.
# Before committing, checks for conflicts. If found, the transaction is rolled back.
# Useful when conflicts are rare.


# 4. Multiversion Concurrency Control (MVCC) (ബഹുസംവേദന സമകാലിക നിയന്ത്രണം):
# Keeps multiple versions of data.
# Allows readers to view data without blocking writers.
# Each transaction sees a snapshot of the data as it was when the transaction began.