class person:
    def __init__(self,name):
        self.name = name
        self._id = 101
        self.__salary = 50000
        
    def display(self):
        print(f"I am {self.name} my id is {self._id}")
    
    def get_salary(self):
        return self.__salary
        
    def set_salary(self,newsalary):
        if newsalary > 0:
            self.__salary += newsalary
            print("Salary Updated SuccesFully")
        else:
            print("Invalid Salary")
            
p1= person("Ashfaque")
p1.display()
print(p1.get_salary())
print(p1.set_salary(10000))
print(p1.get_salary())


