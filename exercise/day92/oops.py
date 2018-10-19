class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self, first, last, sal):
        self.first=first
        self.last=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
        employee.num_employee+=1
    def fullname (self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise (self):
        self.sal=int(self.sal* raise_amount)
 
class developer(employee):
    raise_amount = 1.10
 
emp_1=developer('aayushi', 'johari', 1000000)
print(emp_1.raise_amount)
