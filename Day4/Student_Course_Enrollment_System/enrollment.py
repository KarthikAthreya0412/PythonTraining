from config import get_connection
from mysql.connector import Error

class Enrollment:
    def add_enrollment(self, student_id, course_id, enrollment_date):
        if not student_id or not course_id or not enrollment_date:
            raise ValueError("insufficient data.")

        try:
            conn = get_connection()
            cursor = conn.cursor()

            
            cursor.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
            if cursor.fetchone() is None:
                raise ValueError(f"Student ID {student_id} does not exist.")

            cursor.execute("SELECT * FROM courses WHERE course_id=%s", (course_id,))
            if cursor.fetchone() is None:
                raise ValueError(f"Course ID {course_id} does not exist.")

            cursor.execute(
                "SELECT * FROM enrollments WHERE student_id=%s AND course_id=%s",
                (student_id, course_id)
            )
            if cursor.fetchone():
                raise ValueError("Student is already enrolled in this course.")

            cursor.execute(
                "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)",
                (student_id, course_id, enrollment_date)
            )
            conn.commit()
            print(f"Student ID {student_id} enrolled in Course ID {course_id} successfully.")

        except Error as ee:
            print(f"Enrollment Error: {ee}")

        except Error as e:
            print(f"Database Error: {e}")

        finally:
            cursor.close()
            conn.close()
