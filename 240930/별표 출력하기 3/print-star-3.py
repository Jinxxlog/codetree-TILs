n = int(input())
s = n

for i in range(n):
    print(" " * (i*2), end='')
    for j in range((s*2) - 1):
        print("* ", end = '')
    s -=1

    print()