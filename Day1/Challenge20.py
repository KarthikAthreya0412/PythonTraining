n = int(input())
arr = list(map(int, input().split()))

mini = arr.index(min(arr))
maxi = arr.index(max(arr))

print(maxi - mini)
