a, b = map(int, input().split())
#n = int(input())
sm = 0
cnt = 0

for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        sm += i

print(sm)