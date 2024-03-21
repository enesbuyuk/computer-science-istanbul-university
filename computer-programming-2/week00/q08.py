try:
    c = int(input("Fahrenhayta çevirilecek santigrat sıcaklığını giriniz: "))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
f = 9/5*c+32
print(f"""\nFahrenhayt: {f}""")