operation_history = {'-': [], '+': [], '*': [], '/': []}
while True:
    a = int(input())
    b = int(input())
    c = input()

    if c == '-':
        d = a-b
        f = f"{a} {c} {b} = {d}"
        operation_history['-'].append(f)
    elif c == '+':
        d = a + b
        f = f"{a} {c} {b} = {d}"
        operation_history['+'].append(f)
    elif c == '*':
        d = a*b
        f = f"{a} {c} {b} = {d}"
        operation_history['*'].append(f)
    elif c == '/':
        d = a/b
        f = f"{a} {c} {b} = {d}"
        operation_history['/'].append(f)
    else:
        f = "Операция не поддерживается"
    print(f)
    print(f"+ {operation_history["+"]}")
    print(f"- {operation_history["-"]}")
    print(f"* {operation_history["*"]}")
    print(f"/ {operation_history["/"]}")
