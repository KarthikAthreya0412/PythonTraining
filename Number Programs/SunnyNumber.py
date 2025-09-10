import math

num = int(input("Enter a number: "))

if math.isqrt(num + 1) ** 2 == num + 1:
    print(num, "is a Sunny Number")
else:
    print(num, "is NOT a Sunny Number")
