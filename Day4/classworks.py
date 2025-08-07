   
#     def __init__(self,name,balance):
#         self.name = name;
#         self.balance = balance;
        
#     def checkBalance(self):
#         print(f"{self.name} Balance in {self.balance}");
        
#     def deposit(self,amount):
#         self.balance += amount;
#         print(f"{self.name} Balance in {self.balance}");
        
#     def withDraw(self,amount):
#         self.balance -=amount;
#         print(f"{self.name} Balance in {self.balance}");
        
        
# user1 = Atm("Ashfaque",20000);
# user1.checkBalance();
# user1.deposit(20000);
# user1.withDraw(4000);
# print(user1.bank_name)


# Duck Typing
# class Duck:
#     def Walk(self):
#         print("Duck Is Quacking");
        
# class Human:
#     def Walk(self):
#         print("Human is walking");
        
# def call(think):
#     think.Walk();
    
# call(Duck());
# call(Human());


# Public
# Private
# Protected
# This Are Access Modifiers

# class A:
#     def __init__(self):
#         self.public_var = 'public'
#         self._protected = "Protected"
#         self.__private = "Private"
        
        
# o = A()
# print(o.public_var)
# print(o._protected)
# print(o.__private)    not Supported
# print(o._A__private)  Supported