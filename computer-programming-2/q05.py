try:
    T = int(input("Bilgisayarın satış fiyatını giriniz: "))
    P = int(input("Prim oranını yüzdesini giriniz: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
prim = T*P/100
print(f"\nSatış elemanının bu satışta alacağı prim: {prim}")