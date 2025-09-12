from student import Student
from course import Course
from enrollment import Enrollment
from datetime import date

student=Student()
course=Course()
enrollment=Enrollment()

#add students
#student.add_student("Harri","harri@gmail.com")
#student.add_student("Kisan","kisan@gmail.com")
student.list_enrolled_courses(1)

#add courses
#course.add_course("Python beginner level",4)
#course.add_course("Python intermediate level",5)

# Enroll courses
#enrollment.add_enrollment(1,1,date.today())

