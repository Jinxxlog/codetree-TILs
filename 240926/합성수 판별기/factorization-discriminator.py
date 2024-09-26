n = int(input())
bit = False

for i in range(2, n):
    if n % i == 0:
        bit = True
        break

if bit == True:
    print("C")
else:
    print("N")