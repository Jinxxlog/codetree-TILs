n = int(input())
cnt = 0

for i in range(1, n+1):
    if i % 3 == 0 and i % 9 != 0 or i % 2 == 0 or i % 5 == 0:
        continue
    print(i, end = ' ')