def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def isemirp(n):
    if not isprime(n):
        return False
    reversed_n = int(str(n)[::-1])
    if n == reversed_n:
        return False
    return isprime(reversed_n)

num = int(input("Enter a number: "))
if isemirp(num):
    print(num, "is an Emirp number")
else:
    print(num, "is not an Emirp number")
