class employee:
    def __init__(self, first, last, sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
 
    def fullname(self):
            return '{}{}'.format(self.fname,self.lname)
 
emp_1=employee('sonam','gupta',350000)
emp_2=employee('test','test',100000)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())
