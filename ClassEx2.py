class Emp:
    def __init__(self,id,name,salary):
        self.id = id
        self.name=name
        self.salary = salary
    def display(self):

        print("ID: ",self.id,end=" ")
        print("Name: ",self.name,end = " ")
        print("Salary: ",self.salary,end=" ")
class Emp2:
    @staticmethod
    def disp(e):

        e.display()

e1=Emp(1,"Raj",1000)
#e1.display()
Emp2.disp(e1)