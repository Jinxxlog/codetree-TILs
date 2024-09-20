#a, b = map(int, input().split())
#n = int(input())
sm = 0
cnt = 0

for i in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        sm += a
        cnt += 1

print(sm, round(sm/cnt, 1))