n = int(input())
sm = 1

for i in range(1, 11):
    sm *= i
    if sm >= n:
        print(i)
        break