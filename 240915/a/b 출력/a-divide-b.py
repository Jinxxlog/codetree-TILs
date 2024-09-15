a, b = map(int, input().split())
m = 0

print("0.", end='')

for i in range(20):
    print((a * 10) // b, end='')
    a = (a * 10) % b