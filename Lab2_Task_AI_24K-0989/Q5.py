class Student:
    def __init__(self,name):
        self.name=name

    def set_grade(self,grade):
        self.grade=grade

    def get_grade(self):
        return self.grade
    
    def Display(self):
        print(f"Student name is {self.name} and numbers is {self.grade}")
    

S1=Student("Muhammad Umar")
S2=Student("Salman")

S1.set_grade('A-')
S1.get_grade()

S2.set_grade('B')
S2.get_grade()

S1.Display()
S2.Display()