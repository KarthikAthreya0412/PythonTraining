students={"Asha":78,"Bala":90,"Chitra":65}
result=dict(sorted(students.items(),key=lambda x:x[1],reverse=True))
print(result)