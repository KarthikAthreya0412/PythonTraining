n = int(input())
arr = list(map(int, input().split()))

max_count = 0
max_digit = arr[0]

for digit in arr:
    count = arr.count(digit)
    if count > max_count:
        max_count = count
        max_digit = digit

print(max_digit)
