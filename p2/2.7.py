import msvcrt as m
k = b'n'
while True:
    n = int(input("podaj liczbe n:"))
    wynik = 0
    for i in range(100,1000):
        if (i%10+int(i/10)%10+int(i/100)%10)==n:
            wynik += 1
            print(i)
    print("ilosc liczb:",wynik)
    print("czy chcesz powtorzyc program (T/N)")
    k = m.getch().lower()
    
    print(k)