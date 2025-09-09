n = int(input())
arr = list(map(int, input().split()))

p = set([0])
for num in arr:
    new = set()
    for s in possible_sums:
        new.add(s + num)
    p.update(new)

min_val = min(arr)
m = min_val + 1
while m in arr or m in p:
    m += 1

print(m)
