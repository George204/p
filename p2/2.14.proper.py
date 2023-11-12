import msvcrt as m
k = b'n'
while True:
    n = 0
    while True:
        try:
            n = int(input("podaj wartosc n:"))
            break
        except ValueError:
            print("podaj int")
    a,b = 1,1
    if n>2:
        for i in range(3,n+1):
            a,b = b,a+b
    print(f"{n} wyraz ciagu fibonacciego to {b}")
    print("czy chcesz powtorzyc program (T/N)")
    k = m.getch().lower()
    if k != b't':
        break