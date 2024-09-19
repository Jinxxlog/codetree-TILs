# a, b = map(int, input().split())
n = int(input())
sm = 0

for i in range(n, 101):
    sm += i

print(sm)