from config import get_connection
from mysql.connector import Error

class Course:
    def add_course(self, course_name, credits):
        try:
            if not course_name or credits is None:
                raise ValueError("insufficient data.")

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO courses (course_name, credits) VALUES (%s, %s)",
                (course_name, credits)
            )
            conn.commit()
            print(f"Course {course_name} added successfully.")
        except ValueError as ve:
            print(f"Validation Error: {ve}")
        except Error as e:
            print(f"Database Error while adding course: {e}")
        finally:
            cursor.close()
            conn.close()
