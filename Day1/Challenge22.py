n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

if total % 2 == 0 and total % 3 == 0 and total % 5 == 0:
    print(1)
else:
    print(0)
