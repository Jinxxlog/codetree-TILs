a, b, c = map(int, input().split())
bit = True

for i in range(a, b+1):
    if i % c == 0:
        bit = False
        break

if bit:
    print("YES")
else:
    print("NO")