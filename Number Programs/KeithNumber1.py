num = int(input("Enter a number: "))
num_str = str(num)
digits = [int(d) for d in num_str]
n = len(digits)

temp = sum(digits)

# To Generate sequence until temp >= num
while temp < num:
    digits.append(temp)
    temp = sum(digits[-n:])

if temp == num:
    print(num, "is a Keith Number")
else:
    print(num, "is NOT a Keith Number")
