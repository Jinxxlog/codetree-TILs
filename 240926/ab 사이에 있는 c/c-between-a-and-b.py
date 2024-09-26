a, b, c = map(int, input().split())
bit = False

for i in range(a, b + 1):
    if i % c == 0:
        bit = True
        break

if bit == True:
    print("YES")
else:
    print("NO")