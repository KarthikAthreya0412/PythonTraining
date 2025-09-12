from student import StudentDB

db=StudentDB()

#Add students
#db.add_student("John",28,"A","john@gmail.com")
#db.add_student("Charles",27,"S","charles@gmail.com")

#List all students

db.list_students()

#Update students
db.update_student("John",23,"B","ohn@gmail.com")

db.delete_student("Charles")