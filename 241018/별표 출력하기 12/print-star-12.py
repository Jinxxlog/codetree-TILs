n = int(input())

print('* ' * n)
    
for i in range(1, n):
    line = ''
    for j in range(n):
        if j == 1 or (j > 1 and j % 3 == 1 and i < j):
            line += '* '
        else:
            line += '  '
    print(line.rstrip())