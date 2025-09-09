from functools import reduce
dimentions=[2,3,5]
result=reduce(lambda x,y:x*y,dimentions)
print(result)