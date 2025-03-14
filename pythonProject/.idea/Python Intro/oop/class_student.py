class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        num_of_grades = len(self.grades)
        total = sum(x for x in self.grades)
        return total // num_of_grades

    def display_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)


student = Student("Sristy", 17, [10, 9, 10, 5, 8, 8.5])
print(student.average_grade())
student.display_information()
