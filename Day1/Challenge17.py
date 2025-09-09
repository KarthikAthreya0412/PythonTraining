n, x = map(int, input().split())

wait_time = (n - 1) * 10 - (n - 1) * x

if wait_time < 0:
    wait_time = 0

print(wait_time)
