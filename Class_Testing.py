# Class is a blueprint for creating instances

class Employee:

    no_of_employee = 0
    raise_ratio = 1.04
    def __init__(self, first, last, pay): # Self is passing of the instance itself. Eg: pass emp_1 and then pass emp name, salary etc
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "."+last+"@company.com"
        Employee.no_of_employee += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_ratio)
        #self.pay = int(self.pay * self.raise_ratio)


emp_1 = Employee('Ryu', 'Amano', 50000)  # Instances of the class
emp_2 = Employee('Tina', 'Ben', 10000)


print(emp_1.email) # We are not inputing email as a parameter but the class instance can still access it

print(emp_1.fullname()) # We can access functions like this OR
print(Employee.fullname(emp_1)) # We can also access functions like this

print(emp_1.pay)
emp_1.apply_raise() #Apply raise is using raise_ratio variable
print(emp_1.pay)

print(Employee.raise_ratio)
print(emp_1.raise_ratio) # We are able to access this class variable even when its not defined in the def

print(emp_1.__dict__) # Name space of emp_1. Please notice that it dosen't have raise_ratio
print(Employee.__dict__) # Note that it has raise_ratio

print(Employee.no_of_employee)