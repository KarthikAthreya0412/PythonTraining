import inspect
import student

def test_add_student_query():
    db=student.StudentDB()
    excepted_query="select *from students"
    actual_query=inspect.getsource(db.list_students)
    assert excepted_query in actual_query

def test_update_student_query():
    db=student.StudentDB()
    excepted_query="UPDATE students SET age=%s ,grade=%s ,email=%s where name=%s"
    actual_query=inspect.getsource(db.update_student)
    assert excepted_query in actual_query

def test_delete_student_query():
    db=student.StudentDB()
    excepted_query="Delete from students where name=%s"
    actual_query=inspect.getsource(db.delete_student)
    assert excepted_query in actual_query

def test_add_student():
    sig=inspect.signature(student.StudentDB.add_student)
    assert list(sig.parameters.keys())==["self","name","age","grade","email"]

def test_list_student():
    sig=inspect.signature(student.StudentDB.list_students)
    assert list(sig.parameters.keys())==["self"]

def test_update_student():
    sig=inspect.signature(student.StudentDB.update_student)
    assert list(sig.parameters.keys())==["self","name","age","grade","email"]

def test_delete_student():
    sig=inspect.signature((student.StudentDB.delete_student))
    assert list(sig.parameters.keys())==["self","name"]

    