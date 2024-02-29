try:
    saat = int(input("İşçinin bu hafta çalıştığı toplam saat: "))
    saatlik_ucret = int(input("İşçinin saatlik ücreti: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
brut = saat*saatlik_ucret
net =  brut - brut*0.15
print(f"""\nİşçinin brüt maaşı: {brut}
İşçinin net maaşı: {net}""")