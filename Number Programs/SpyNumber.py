num = int(input("Enter a number: "))
temp = num
sum_digits = 0
prod_digits = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    prod_digits *= digit
    temp //= 10

if sum_digits == prod_digits:
    print(num, "is a Spy Number")
else:
    print(num, "is NOT a Spy Number")
