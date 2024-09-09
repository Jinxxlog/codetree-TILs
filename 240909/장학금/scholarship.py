a, b = map(int, input().split())

if a >= 90:
    if b < 90:
        print(0)
    elif b < 95:
        print(5)
    else:
        print(10)
else:
    print(0)