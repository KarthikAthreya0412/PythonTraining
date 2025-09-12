import inspect
import student
import course
import enrollment

# ---------------- Student Tests ----------------
def test_add_student_query():
    db = student.Student()
    expected_query = "INSERT INTO students (name, email) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.add_student)
    assert expected_query in actual_query

def test_add_student_signature():
    sig = inspect.signature(student.Student.add_student)
    assert list(sig.parameters.keys()) == ["self", "name", "email"]

def test_list_enrolled_courses_signature():
    sig = inspect.signature(student.Student.list_enrolled_courses)
    assert list(sig.parameters.keys()) == ["self", "student_id"]

# ---------------- Course Tests ----------------
def test_add_course_query():
    db = course.Course()
    expected_query = "INSERT INTO courses (course_name, credits) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.add_course)
    assert expected_query in actual_query

def test_add_course_signature():
    sig = inspect.signature(course.Course.add_course)
    assert list(sig.parameters.keys()) == ["self", "course_name", "credits"]

# ---------------- Enrollment Tests ----------------
def test_add_enrollment_insert_query():
    db = enrollment.Enrollment()
    expected_query = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(db.add_enrollment)
    assert expected_query in actual_query

def test_add_enrollment_check_student_query():
    db = enrollment.Enrollment()
    expected_query = "SELECT * FROM students WHERE student_id=%s"
    actual_query = inspect.getsource(db.add_enrollment)
    assert expected_query in actual_query

def test_add_enrollment_check_course_query():
    db = enrollment.Enrollment()
    expected_query = "SELECT * FROM courses WHERE course_id=%s"
    actual_query = inspect.getsource(db.add_enrollment)
    assert expected_query in actual_query

def test_add_enrollment_check_duplicate_query():
    db = enrollment.Enrollment()
    expected_query = "SELECT * FROM enrollments WHERE student_id=%s AND course_id=%s"
    actual_query = inspect.getsource(db.add_enrollment)
    assert expected_query in actual_query

def test_add_enrollment_signature():
    sig = inspect.signature(enrollment.Enrollment.add_enrollment)
    assert list(sig.parameters.keys()) == ["self", "student_id", "course_id", "enrollment_date"]
