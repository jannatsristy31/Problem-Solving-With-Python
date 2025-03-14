class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.courses_enrolled = []

    def enroll(self, course):
        if course not in self.courses_enrolled:
            self.courses_enrolled.append(course)
            course.add_student(self)
            print(f"{self.name} has been enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")

    def unenroll(self, course):
        if course in self.courses_enrolled:
            self.courses_enrolled.remove(course)
            course.remove_student(self)
            print(f"{self.name} has been unenrolled from {course.name}.")
        else:
            print(f"{self.name} is not enrolled in {course.name}.")

    def list_courses(self):
        if self.courses_enrolled:
            print(f"Courses enrolled by {self.name}:")
            for course in self.courses_enrolled:
                print(f"- {course.name}")
        else:
            print(f"{self.name} is not enrolled in any courses.")


class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def list_students(self):
        if self.enrolled_students:
            print(f"Students enrolled in {self.name}:")
            for student in self.enrolled_students:
                print(f"- {student.name}")
        else:
            print(f"No students are enrolled in {self.name}.")


class Enrollment:
    @staticmethod
    def create_student(student_id, name, dob):
        return Student(student_id, name, dob)

    @staticmethod
    def create_course(course_id, name, description):
        return Course(course_id, name, description)

    @staticmethod
    def display_enrollment_table(courses):
        if not courses:
            print("No enrollment data to display.")
            return

        print("Enrollment Information:")
        # Remember this ({:<20} {:<20}) for now; we'll go over it later when I can explain it more clearly.
        print("=" * 40)
        print("{:<20} {:<20}".format("Course Name", "Enrolled Students"))

        for course in courses:
            course_name = course.name
            print([student.name for student in course.enrolled_students])
            enrolled_students = ", ".join([student.name for student in course.enrolled_students])
            # Remember this ({:<20} {:<20}) for now; we'll go over it later when I can explain it more clearly.
            print("=" * 40)
            print("{:<20} {:<20}".format(course_name, enrolled_students))

        print("=" * 40)


if __name__ == "__main__":

    # Create new students
    student1 = Enrollment.create_student(1, "Asif", "1999-05-15")
    student2 = Enrollment.create_student(2, "Fatin", "2000-03-20")

    # Create new courses
    course1 = Enrollment.create_course(101, "Mathematics", "Advanced Calculus")
    course2 = Enrollment.create_course(102, "Methodology", "Python Programming")

    # Enroll students in courses
    student1.enroll(course1)
    student1.enroll(course2)
    student2.enroll(course2)

    # Display enrollment information
    courses = [course1, course2]
    Enrollment.display_enrollment_table(courses)
