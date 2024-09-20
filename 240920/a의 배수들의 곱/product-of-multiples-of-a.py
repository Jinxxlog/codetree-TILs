a, b = map(int, input().split())
#n = int(input())
prod = 1
cnt = 0

for i in range(1, b+1):
    if i % a == 0:
        prod *= i

print(prod)