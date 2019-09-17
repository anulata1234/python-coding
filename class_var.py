





class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+ '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)



emp_1 = Employee("anu", "singh", 50000)
emp_2 = Employee("Test", "1s3", 60000)

print(Employee.num_of_emps)
