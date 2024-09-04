n, m = map(int, input().split())

def star(n, m):
    for i in range(n):
        for i in range(m):
            print(1, end='')
        print()

star(n, m)