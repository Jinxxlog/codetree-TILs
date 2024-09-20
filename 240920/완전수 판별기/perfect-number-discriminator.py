#a, b = map(int, input().split())
n = int(input())
sm = 0
cnt = 0

for i in range(1, n):
    if n % i == 0:
        sm += i

if sm == n:
    print("P")
else:
    print("N")