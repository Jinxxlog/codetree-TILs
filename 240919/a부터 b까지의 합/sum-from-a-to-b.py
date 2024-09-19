a, b = map(int, input().split())
sm = 0

for i in range(a, b+1):
    sm += i

print(sm)