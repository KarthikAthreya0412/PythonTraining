num = int(input("Enter a number: "))

if num % 7 == 0 or str(num).endswith('7'):
    print(num, "is a Buzz number")
else:
    print(num, "is not a Buzz number")
