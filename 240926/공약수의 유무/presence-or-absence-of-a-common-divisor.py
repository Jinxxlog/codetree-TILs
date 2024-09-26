a, b = map(int, input().split())
bit = False

for i in range(a, b + 1):
    if 1920%i == 0 or 2880%i == 0:
        bit = True
        break

if bit == True:
    print(1)
else:
    print(0)