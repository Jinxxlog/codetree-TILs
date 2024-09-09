s = int(input())
age = int(input())

if s == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
elif s == 1:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")