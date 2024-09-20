a, b = map(int, input().split())
#n = int(input())
prod = 1
cnt = 0

for i in range(a, b+1):
    prod *= i

print(prod)