a, b = map(int, input().split())
n = 0

print(a//b, end='')
print(".", end='')

while n < 20:
    if a <= b:
        print((a * 10) // b, end='')
        a = (a * 10) % b
        n += 1
    else:
        a = a % b