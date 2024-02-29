try:
    a = int(input("Prizmanın a yüzeyini giriniz: "))
    b = int(input("Prizmanın b yüzeyini giriniz: "))
    c= int(input("3Prizmanın c yüzeyini giriniz: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
yuzey_alani = 2*(a*b+b*c+c*a)
print(f"\nPrizmanın Yüzey Alanı: {yuzey_alani}")
