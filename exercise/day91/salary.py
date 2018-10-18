class employee:
    perc_raise =1.05
    def __init__(self, first, last, sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
 
    def fullname(self):
            return '{}{}'.format(self.fname,self.lname)
    def apply_raise(self):
        self.sal=int(self.sal*1.05)
 
emp_1=employee('aayushi','johari',350000)
emp_2=employee('test','test',100000)
 
print(emp_1.sal)
emp_1.apply_raise()
print(emp_1.sal)
