try:
    k1 = int(input("K1 değerini giriniz: "))
    k2 = int(input("K2 değerini giriniz: "))
    n = int(input("N değerini giriniz: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
x=n/(k1+k2)
print(f"""\nİki karo ustası birlikte {n} adet karoyu {x} saatte döşer.""")
