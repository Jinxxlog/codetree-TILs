cnt = 0

for i in range(3):
    a = input().split()
    if a[0] == "Y" and int(a[1]) >= 37:
        cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")