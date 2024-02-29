try:
    n = float(input("N değerini giriniz: "))
    y1 = float(input("1. yıl yüzdesel oranını -y1- giriniz: "))
    y2 = float(input("2. yıl yüzdesel oranını -y2- giriniz: "))
    y3 = float(input("3. yıl yüzdesel oranını -y3- giriniz: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
y1_odeme=n*y1/100
y2_odeme=n*y2/100
y3_odeme=n*y3/100
print(f"""\n1. yıl ödenecek para miktarı:{y1_odeme}
2. yıl ödenecek para miktarı:{y2_odeme}
3. yıl ödenecek para miktarı:{y3_odeme}""")