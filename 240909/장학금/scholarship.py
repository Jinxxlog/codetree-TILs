a, b = map(int, input().split())

if a >= 90:
    if b < 90:
        print(0)
    elif b < 95:
        print(50000)
    else:
        print(100000)
else:
    print(0)