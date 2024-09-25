n = int(input())
de = 2
cnt = 1

while True:
    if n == de:
        break
    de *= 2
    cnt += 1

print(cnt)