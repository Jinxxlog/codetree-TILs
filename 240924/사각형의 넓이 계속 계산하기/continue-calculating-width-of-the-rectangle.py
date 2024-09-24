cnt = 0

while True:
    x, y, c = input().split()
    
    print(int(x) * int(y))
        
    if c == 'c' or c == 'C':
        break