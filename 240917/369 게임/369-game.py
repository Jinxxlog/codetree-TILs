n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end = ' ')
    elif 3 in map(int, str(i)) or 6 in map(int, str(i)) or 9 in map(int, str(i)):
        print(0, end = ' ')
    else:
        print(i, end = ' ')