sm = 0
cnt = 0

while True:
    n = int(input())
    if n >= 30:
        break
    cnt += 1
    sm += n

print(format(sm/cnt, ".2f"))