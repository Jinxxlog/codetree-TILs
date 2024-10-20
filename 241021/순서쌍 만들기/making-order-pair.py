n = int(input())

for i in range(n, 0, -1):
    row = []
    for j in range(n, 0, -1):
        row.append(f"({i},{j})")
    print(" ".join(row))