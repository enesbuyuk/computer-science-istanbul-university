try:
    a = int(input("a sayısını giriniz:"))
    b = int(input("b sayısını giriniz:"))
    c= int(input("c sayısını giriniz:"))
except ValueError:
    print("Lütfen sayı değeri giriniz!")
x = (c-b)/a
print(x)