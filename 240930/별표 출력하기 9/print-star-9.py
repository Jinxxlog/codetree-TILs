n = int(input())
s = n-1

for i in range(1, n+1):
    print(" " * (s*2), end='')
    for j in range((i*2)-1):
        print("* ", end = '')
    s -=1

    print()