
class Employee:
    def __init__(self,name,sal,addr):
        self.n = name
        self.s = sal
        self.addr = addr

    def disp(self):
        print("Name: ",self.n)
        print("Sal: ",self.s)

class Emp(Employee):
    def display(self):
        Employee.disp(self)
        print("Addr: ",self.addr)


e2=Emp("Kumar",2000,"BLR")
e2.display()

# e1=Employee("Raj",3000,"CHE")
# e1.disp()



