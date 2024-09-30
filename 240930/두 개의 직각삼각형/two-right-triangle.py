n = int(input())
s = n-1

for i in range(n, 0, -1):
    print("*" * (i), end='')
    print(" " * ((n-i)*2), end='')
    print("*" * (i), end='')
    print()