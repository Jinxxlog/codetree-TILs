n, m = map(int, input().split())

def log(n, m):
    while n > 0:
        m, n = n, m%n
    print(m)

log(n, m)