indirim_esigi = int(input("indirim esigini giriniz:"))
indirim_orani = int(input("indirim oranını giriniz:"))
fiyat = int(input("ürün fiyatını giriniz"))
if(fiyat >= indirim_esigi):
    indirimli_fiyat = fiyat - fiyat*indirim_orani/100
    print(f"İndirimli fiyat {indirimli_fiyat}")
else:
    print("ürün fiyatı indirim eşiği altında kalmaktadır.")