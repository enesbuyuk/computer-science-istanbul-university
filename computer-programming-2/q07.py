try:
    cap = int(input("Çemberin çapını giriniz: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
cember_uzunluk = 22/7*cap
print(f"""\nÇemberin uzunluğu: {cember_uzunluk}""")
