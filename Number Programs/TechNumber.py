num = int(input("Enter a number: "))
num_str = str(num)
n = len(num_str)

if n % 2 == 0:  # Check even digits
    first_half = int(num_str[:n//2])
    second_half = int(num_str[n//2:])
    if (first_half + second_half) ** 2 == num:
        print(num, "is a Tech Number")
    else:
        print(num, "is NOT a Tech Number")
else:
    print(num, "is NOT a Tech Number")
