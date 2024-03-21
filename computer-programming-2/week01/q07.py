print("Doğu: negatif, Batı:pozitif")
a = int(input("a aracının gittiği mesafeyi giriniz:"))
b= int(input("b aracının gittiği mesafeyi giriniz:"))
if(abs(a) == abs(b)):
    print("iki araç da aynı mesafe yol katetti.")
elif(abs(a) > abs(b)):
    print("a aracı daha fazla yol katetti")
else:
    print("b aracı daha fazla yol katetti")