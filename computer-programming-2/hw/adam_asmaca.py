import random

sozluk = ["elma", "armut", "kagit", "kalem"]
kelime = random.choice(sozluk)
tahmin_edilen_harfler = []
gorunen_kelime = ["_" for _ in range(len(kelime))]
can = 6
print("""
 _______ _____  _______ _______ _______ _______ _______ _______ ______ _______ 
|   _   |     \|   _   |   |   |   _   |     __|   |   |   _   |      |   _   |
|       |  --  |       |       |       |__     |       |       |   ---|       |
|___|___|_____/|___|___|__|_|__|___|___|_______|__|_|__|___|___|______|___|___|
                                                                               
""")
print("github.com/enesbuyuk\nwww.EnesBuyuk.com")
cubuk_ust="""
  +---+
  |   |"""
cubuk_alt="""
      |
=========
"""
can_6 = cubuk_ust+"""
      |
      |
      |
      |"""+cubuk_alt
can_5 = cubuk_ust+"""
  O   |
      |
      |
      |"""+cubuk_alt
can_4 = cubuk_ust+"""
  O   |
  |   |
      |
      |"""+cubuk_alt
can_3 = cubuk_ust+"""
  O   |
 /|   |
      |
      |"""+cubuk_alt
can_2 = cubuk_ust+"""
  O   |
 /|\  |
      |
      |"""+cubuk_alt
can_1 = cubuk_ust+"""
  O   |
 /|\  |
 /    |
      |"""+cubuk_alt
can_0 = cubuk_ust+"""
  O   |
 /|\  |
 / \  |
      |"""+cubuk_alt
canlar = [can_0, can_1, can_2, can_3, can_4,can_5,can_6]
while True:
    print(canlar[can])
    if "_" not in gorunen_kelime:
        print(f"\"{kelime}\" kelimesini başarıyla tahmin ettiniz.\n Oyun bitti.")
        break
    else:
        if can <= 0:
            print(f"Kelime tahmin etmek için hakkınız bitmiştir!\nOyun bitti.\n")
            break
    harf = input(f"\nKelime için bir harf tahmin ediniz: ").lower()
    if harf.isalpha() and len(harf) == 1:
        if harf not in tahmin_edilen_harfler:
            tahmin_edilen_harfler.append(harf)
            if harf in kelime:
                for x in range(len(kelime)):
                    if harf == kelime[x]:
                        gorunen_kelime[x] = harf
            else:
                print(f"Maalesef, seçilen kelimede \"{harf}\" harfi bulunmamaktadır.")
                can -= 1
        else:
            print("Bu harf daha önce tahmin edildi.")
        print("".join(gorunen_kelime))
    else:
        print("Lütfen bir harf giriniz.")
