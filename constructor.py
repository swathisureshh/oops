# class Student:
#     def __init__(self,name,roll,branch):
#         self.name=name
#         self.roll=roll
#         self.branch=branch
#     def displayDeatiles(self):
#         print('Name is:',self.name)
#         print('Roll is:',self.roll)
#         print('Branch is:',self.branch)
#         print()
        
# s1=Student("Swathi",15,"ECE")
# s1.displayDeatiles()

class Employee:
    def __init__(self):
        self.name="swathi"
        self.id=2034567
        self.role='python dev'
        self.salary=78000.0
        self.company='accenture'
    def display(self):
        print('Name is:',self.name)
        print('Id is',self.id)
        print('Role is',self.role)
        print('salary is',self.salary)
        print('company is',self.company)
        print()
e1=Employee()
e2=Employee()
e1.display()
e2.display()
        
        