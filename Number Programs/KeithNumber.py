num = int(input("Enter a number: "))
square = num * num
sum_digits = 0

while square > 0:
    digit = square % 10
    sum_digits += digit
    square //= 10

if sum_digits == num:
    print(num, "is a Neon Number")
else:
    print(num, "is NOT a Neon Number")
