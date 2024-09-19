# a, b = map(int, input().split())
n = int(input())
sm = 0

for i in range(n):
    a = int(input())
    if a % 2 != 0 and a % 3 == 0:
        sm += a

print(sm)