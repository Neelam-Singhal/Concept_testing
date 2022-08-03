# Class is a blueprint for creating instances

class Employee:
    def __init__(self, first, last, pay): # Self is passing of the instance itself. Eg: pass emp_1 and then pass emp name, salary etc
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "."+last+"@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee('Ryu', 'Amano', 13)  # Instances of the class
#emp_2 = Employee()


print(emp_1.email)
print(emp_1.fullname())


print(Employee.fullname(emp_1))
