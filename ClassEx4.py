
class Employee:
    def __init__(self,name,sal):
        self.n = name
        self.s = sal
    def disp(self):

        print("Name: ",self.n)
        print("Sal: ",self.s)


class Emp(Employee):
    def display(self,addr):
        self.addr = addr
        Employee.disp(self)
        print("Addr: ",self.addr)


e2=Emp("Kumar",2000)
e2.display("BLR")
#e2.display("CHE")







