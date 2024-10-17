n = int(input())

for i in range(n*3-(n-1)): 
    for j in range(n*3-(n-1)):
        if i % 2 == 0 or j % 2 == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()