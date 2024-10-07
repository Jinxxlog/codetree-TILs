n = int(input())

for i in range(n, 0, -1): 
    for h in range((n-i)*2):
        print(' ', end='')

    for j in range((i*2)-1, 0, -1):
        print('*', end=' ')
    print()

for i in range(2, n+1):
    for h in range((n-i)*2):
        print(' ', end='')
        
    for j in range((i*2)-1, 0, -1):
        print('*', end=' ')
    print()