a, b, c = map(int, input().split())



print(int(a == min(a, b, c)), end = ' ')
print(int(a == b and b == c and c == a), end = ' ')