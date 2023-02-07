## --------------------------------------------------------------
## Defines a Student class with the following attributes: 
## - first_name
## - last_name
## - email
## - student_id
## - classes
## - gpa
##
## The first 4 attributes are pretty simple and are set when a new instance is created,
## besides student_id which can later be set using a method.
## 
## Once a Student is created, classes can be added to the self.classes dictionary, which
## contains the class name and associated GPA 
##
## Then, to calculate the students GPA, the calculate_gpa method can be called, which 
## iterates over the classes dictionary and returns the average GPA of each class.
##
## Below is an example of a student and how each of the methods can be used to store 
## information about a student.
## ----------------------------------------------------------------

class Student:
 
    def __init__(self, first_name, last_name, student_id=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name.lower() + last_name.lower() + "@binghamton.edu"

        self.gpa = 0
        self.classes = {}
    
    def add_student_id(self, student_id):

        self.student_id = student_id
    
    def add_class(self, class_name, class_gpa):

        self.classes[class_name] = class_gpa

    def update_class_grade(self, class_name, new_class_gpa):

        self.classes[class_name] = new_class_gpa

    def calculate_gpa(self):

        sum = 0
        for i in self.classes:
            sum = sum + self.classes[i]

        self.gpa = sum / len(self.classes)
        return self.gpa


jake = Student("Jake", "Smith")

jake.add_class("Math", 90)
jake.add_class("Science", 80)
jake.add_class("English", 95)
jake.add_class("History", 85)
jake.update_class_grade("History", 100)
jake.add_student_id(1)

jake.calculate_gpa()
print(jake.classes)
print(jake.gpa)
print(jake.email)
print(jake.student_id)

