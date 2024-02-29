try:
    a = float(input("1. sayıyı giriniz:"))
    b = float(input("2. sayıyı giriniz:"))
    c= float(input("3. sayıyı giriniz:"))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
aritmetik = (a+b+c)/3
harmonik = 3/(1/a+1/b+1/c)
print(f"""\nGirilen 3 reel sayının;
Aritmetik Ortalaması: {aritmetik}
Harmonik Ortalaması: {harmonik}""")

