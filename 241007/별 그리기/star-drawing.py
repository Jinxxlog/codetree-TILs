n = int(input())

for i in range(1, n+1): 
    for h in range(n-i, 0, -1):
        print(' ', end='')

    for j in range((i*2)-1, 0, -1):
        print('*', end='')
    print()

for i in range(n-1, 0, -1): 
    for h in range(n-i, 0, -1):
        print(' ', end='')

    for j in range((i*2)-1, 0, -1):
        print('*', end='')
    print()