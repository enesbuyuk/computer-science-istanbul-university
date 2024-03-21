boy = float(input("boy bilgisini metre cinsinden giriniz:"))
kilo = float(input("kilo bilgisini kg cinsinden giriniz"))
vki = kilo/boy**2
if(vki < 18.5):
    print("zayıf")
elif (vki >= 18.5 and vki < 25):
    print("normal")
elif (vki >= 25 and vki < 30):
    print("kilolu")
else:
    print("obez")
print(f" vucut kitle endeksi: {vki}")