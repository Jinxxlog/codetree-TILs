def ch(n, m):
    u = n * m
    while m != 0:
        n, m = m, n%m
    print(u // n)

n, m = map(int, input().split())
ch(max(n, m), min(n, m))