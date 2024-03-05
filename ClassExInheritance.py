
class Employee:
    def __init__(self,name,sal):
        self.n = name
        self.s = sal

    def disp(self):
        print("Name: ",self.n)
        print("Sal: ",self.s)

class Emp(Employee):
    def display(self):
        print("Name: ", self.n)
        print("Sal: ", self.s)

e1=Employee("Raj",1000)
e1.disp()
e2=Emp("Kumar",2000)
e2.display()




