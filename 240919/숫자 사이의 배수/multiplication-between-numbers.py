a, b = map(int, input().split())
#n = int(input())
sm = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sm += i
        cnt+=1

print(sm, round(sm/cnt, 1))