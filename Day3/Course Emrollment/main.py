from course import Course
from student import Student, PremiumStudent

def main():
    
    c1 = Course("Python Programming", "CS101", 3, 5000)
    c2 = Course("Data Structures", "CS102", 4, 6000)
    c3 = Course("Machine Learning", "CS103", 5, 8000)

    student1 = Student("Aarav")
    student2 = PremiumStudent("Diya")

    student1.enroll_course(c1)
    student1.enroll_course(c2)
    student1.view_courses()
    student1.calculate_total()

    student2.enroll_course(c2)
    student2.enroll_course(c3)
    student2.view_courses()
    student2.calculate_total()

    student1.drop_course("CS101")
    student1.view_courses()
    student1.calculate_total()

if __name__ == "__main__":
    main()
