n = int(input())
lst = []

for i in range(n):
    a = input().split()

    if a[0] == "push_back":
        lst.append(int(a[1]))
    elif a[0] == "pop_back":
        lst.pop()
    elif a[0] == "size":
        print(len(lst))
    else:
        print(lst[int(a[1])-1])