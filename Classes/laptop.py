# Mthod that perfroms action
class student:
    
    def __init__(self,name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display_info(self):
        print(self.name, self.age, self.marks)
    def get_grade(self):
        
        if self.marks >=90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >=50:
            return "C"
        else:
            return "Fail"
        