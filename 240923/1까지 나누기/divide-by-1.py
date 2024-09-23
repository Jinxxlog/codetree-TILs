n = int(input())
res = n
cnt = 0

for i in range(1, n):
    res //= i
    cnt += 1
    if res <= 1:
        print(cnt)
        break