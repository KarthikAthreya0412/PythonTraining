from enrollment import Enrollment

class Student:
    def __init__(self, name):
        self.name = name
        self.enrollment = Enrollment()

    def enroll_course(self, course):
        self.enrollment.enroll(course)

    def drop_course(self, course_code):
        self.enrollment.drop(course_code)

    def view_courses(self):
        print(f"\n{self.name}'s Courses:")
        self.enrollment.display_enrolled_courses()

    def calculate_total(self):
        total = self.enrollment.total_fee()
        print(f"{self.name}'s Total Fee: ₹{total}")
        print(f"Total Credits: {self.enrollment.total_credits()}")

class PremiumStudent(Student):
    def calculate_total(self):
        total = self.enrollment.total_fee()
        discount = total * 0.20
        discounted_total = total - discount
        print(f"{self.name}'s Total Fee with 20% Discount: ₹{discounted_total}")
        print(f"Total Credits: {self.enrollment.total_credits()}")
