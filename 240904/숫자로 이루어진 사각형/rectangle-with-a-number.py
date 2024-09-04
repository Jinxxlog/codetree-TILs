n = int(input())
a = 0

def star(n, a):
    for i in range(n):
        for j in range(n):
            a += 1
            if a >= 10:
                a = 1
            print(a, end=' ')
        print()

star(n, a)