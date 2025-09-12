from config import get_connection
from mysql.connector import Error
 
class StudentDB:
    def add_student(self,name,age,grade,email):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute(
                "insert into students (name,age,grade,email) values (%s,%s,%s,%s)",
                (name,age,grade,email)
            )
            conn.commit()
            print(f"Student {name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
 
    def list_students(self):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("select *from students")
            rows=cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_student(self,name,age,grade,email):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute(
                "UPDATE students SET age=%s ,grade=%s ,email=%s where name=%s",
                (age,grade,email,name)
            )
            conn.commit()
            if cursor.rowcount>0:
                print(f"Student {name} updated successfully")
            else:
                print(f"Student {name} not found")
        except Error as er:
            print("Error: ",er)
        finally:
            cursor.close()
            conn.close()
    def delete_student(self,name):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute(
                "Delete from students where name=%s",(name,)
            )
            conn.commit()
        except Error as er:
            print("Error: ",er)
        finally:
            cursor.close()
            conn.close()
