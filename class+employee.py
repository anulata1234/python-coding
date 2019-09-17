
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+ '.'+last+ '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)


emp_1 = Employee('anu' , 'singh', 50000)
emp_2 = Employee('sneha','singh', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
