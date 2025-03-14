class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        self.teachers = []


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_courses = []

    def enroll_course(self, course):
        self.student_courses.append(course)

    def display_information(self):

        for x in self.student_courses:
            print(x.course_code)



class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.assign_course = []

    def course_assign(self, course):
        self.assign_course.append(course)


class CourseManager:

    def enroll_students_courses(self, student, course):
        student.enroll_course(course)

    def assign_teachers_courses(self, teacher, course):
        teacher.course_assign(course)


school = School("Maple Leaf")
course_1 = Course("Mat116", "Introduction to Calculus")
course_2 = Course("Phi101", "Introduction to Philosophy")
course_3 = Course("Phy107", "Introduction to Physics")
course_4 = Course("CSE173", "Discreet Mathematics")

student_1 = Student(1931533042, "Sadik Ittesaf")
student_2 = Student(1931542042, "Refah Tasnia")
student_3 = Student(1932452042, "Nandini Das")

teacher_1 = Teacher(1942042, "Robert Pattinson")
teacher_2 = Teacher(1915042, "Jacob Elordi")

coursemanage_1 = CourseManager()
coursemanage_1.enroll_students_courses(student_1, course_1)
coursemanage_1.enroll_students_courses(student_1, course_4)

coursemanage_1.enroll_students_courses(student_2, course_1)
coursemanage_1.enroll_students_courses(student_2, course_3)

coursemanage_1.assign_teachers_courses(teacher_1, course_1)
coursemanage_1.assign_teachers_courses(teacher_1, course_3)

coursemanage_1.assign_teachers_courses(teacher_2, course_2)
student_1.display_information()
