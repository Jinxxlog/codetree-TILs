n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

for i in range(n):
    if lst[i] % 2 != 0 and lst[i] % 3 == 0:
        print(lst[i])