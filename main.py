lst = []
while True:
    a = int(input())
    b = int(input())
    c = input()
    if c == '-':
        d = a-b
    if c == '+':
        d = a + b
    if c == '*':
        d = a*b
    if c == '/':
        d = a/b
    #f = (a + c + b + "=" + d)
    f = f"{a} {c} {b} = {d}"
    lst.append(f)
    print(lst)