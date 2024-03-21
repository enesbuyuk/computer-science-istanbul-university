from fractions import Fraction
sayi = float(input("lütfen ondalılı sayıyı giriniz:"))
kesir =Fraction(sayi).limit_denominator(10)
kesirler = []
sayi_f = float(int(sayi))
for i in range(1,11):
    if sayi_f+0.1 > sayi and sayi_f-0.1<sayi:
        onceki = Fraction(sayi_f).limit_denominator(10)
        sonraki = Fraction(sayi_f+0.1 ).limit_denominator(10)
        print(f"yaklaşan 1/10'luk kesirler: {onceki} ---- {sonraki}")
        break
    sayi_f =sayi_f +0.1
print(f"sayinin en sade kesir hali: {kesir}")