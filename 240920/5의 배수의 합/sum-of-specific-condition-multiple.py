a, b = map(int, input().split())
#n = int(input())
sm = 0
cnt = 0

for i in range(min(a, b), max(a, b)+1):
    if i % 5 == 0:
        sm += i

print(sm)