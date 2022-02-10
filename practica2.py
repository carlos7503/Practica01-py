a = int(input("a-->"))
b = int(input("b-->"))
c = int(input("c-->"))
if a >= b  and a >= c:
    print(f"la variable a es la más alta con: {a}")
elif b >= a and b >= c:
    print(f"la variable b es la más alta con: {b}")
elif c >= a and c >= b:
    print(f"la variable c es la más alta con: {c}")
