# Python Object-Oriented programming
# Remove duplicates from sorted array

class Employee:
    # class variables
    pay_raise = 1.04

    def __init__(self, name, address, pay):
        # instance variables
        self.name = name
        self.address = address
        self.pay = pay

    def greet(self):
        return "Hello " + self.name

    def pay_rise(self):
        # return self.pay * Employee.pay_raise
        return self.pay * self.pay_raise


if __name__ == '__main__':
    print("Under main et")
    emp1 = Employee("Jack", "London", 1000)
    print(Employee.greet(emp1))
    print(emp1.greet())
    print(emp1.pay_rise())
    Employee.pay_raise = 1.03
    emp1.pay_raise = 1.05
    print(emp1.pay_rise())
    print(emp1.__dict__)
    print(Employee.__dict__)
