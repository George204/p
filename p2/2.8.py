import msvcrt as m
k = b't'
while True:
    n = 0
    while True:
        n = int(input("ile liczb wprowadzic:"))
        if bool(n) and n>0:
            break
        else:
            print("niprawidlowa wartosc")
    print("test",n)
    print("czy chcesz powtorzyc program (T/N)")
    k = m.getch().lower()
    if k == b'n':
        break