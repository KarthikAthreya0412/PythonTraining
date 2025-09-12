from config import get_connection
from mysql.connector import Error

class Student:
    def add_student(self, name, email):
        try:
            if not name or not email:
                raise ValueError("insufficient data.")

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, email) VALUES (%s, %s)", (name, email)
            )
            conn.commit()
            print(f"Student {name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def list_enrolled_courses(self, student_id):
        try:
            if not student_id:
                raise ValueError("Student ID is required.")

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT c.course_name, c.credits, e.enrollment_date
                FROM enrollments e
                JOIN courses c ON e.course_id = c.course_id
                WHERE e.student_id = %s
                """,
                (student_id,)
            )
            rows = cursor.fetchall()
            if not rows:
                print("No courses found for this student.")
            else:
                print(f"Courses for Student ID {student_id}:")
                for row in rows:
                    print(f"- {row[0]} ({row[1]} credits) | Enrolled on {row[2]}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
