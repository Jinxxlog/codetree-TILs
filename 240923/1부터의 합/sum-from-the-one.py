n = int(input())
sm = 0

for i in range(1, 101):
    sm += i
    if sm >= n:
        print(i)
        break