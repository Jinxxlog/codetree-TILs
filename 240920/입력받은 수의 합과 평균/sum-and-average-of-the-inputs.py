#a, b = map(int, input().split())
n = int(input())
sm = 0
cnt = 0

for i in range(n):
    sm += int(input())

print(sm, round(sm/n, 1))