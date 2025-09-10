class Enrollment:
    def __init__(self):
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Enrolled in {course.name}")
        else:
            print(f"Already enrolled in {course.name}")

    def drop(self, course_code):
        for course in self.courses:
            if course.code == course_code:
                self.courses.remove(course)
                print(f"Dropped {course.name}")
                return
        print("Course not found in enrollment")

    def total_credits(self):
        return sum(course.credits for course in self.courses)

    def total_fee(self):
        return sum(course.fee for course in self.courses)

    def display_enrolled_courses(self):
        print("Enrolled Courses:")
        for course in self.courses:
            course.display_details()
