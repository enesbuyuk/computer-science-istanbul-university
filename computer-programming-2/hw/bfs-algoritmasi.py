from collections import deque


def hareket_sart(labirent, ziyaret, x, y):
    if 0 <= x < len(labirent) and 0 <= y < len(labirent[0]) and labirent[x][y] == 0 and not ziyaret[x][y]:
        return True
    return False


def en_kisa_yolu_bul(labirent):
    """Breadth First Search (BFS) algoritması kullanarak labirentteki en kısa yolu bulur."""
    satir = len(labirent)
    sutun = len(labirent[0])
    bas = (0, 0)
    son = (satir - 1, sutun - 1)
    ziyaret = [[False for _ in range(sutun)] for _ in range(satir)]
    hareketler = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    kuyruk = deque([(bas, [bas])]) # deque kullanarak kuyruk yapısı oluşturuldu

    # BFS algoritması kuyruk yapısını kullanarak en kısa yolu bulur
    while kuyruk:
        (suan_yol, yol) = kuyruk.popleft() # kuyruk'den eleman çıkarıldı
        (x, y) = suan_yol

        if suan_yol == son:
            return yol
        ziyaret[x][y] = True
        for hareket in hareketler:
            yeni_x, yeni_y = x + hareket[0], y + hareket[1]

            if hareket_sart(labirent, ziyaret, yeni_x, yeni_y):
                ziyaret[yeni_x][yeni_y] = True
                kuyruk.append(((yeni_x, yeni_y), yol + [(yeni_x, yeni_y)]))
    return None


matrix_satir = int(input("Matrix'in satır sayısını girin: "))
matrix_sutun = int(input("Matrix'in sütun sayısını girin: "))

matrix = []

print(f"Lütfen {matrix_satir} satır ve {matrix_sutun} sütunlu matrisi girin:")
for i in range(matrix_satir):
    row = [int(x) for x in input().split()]
    for j in row:
        assert j in [0, 1], "Matrix elemanları 0 ve 1 olmalıdır!"
    matrix.append(row)

yol = en_kisa_yolu_bul(matrix)
if yol:
    print("En kısa yol bulundu:", yol)
else:
    print("Yol bulunamadı")
"""
Örnek girdi:
Matrix'in satır sayısını girin: 5
Matrix'in sütun sayısını girin: 5
Lütfen 5 satır ve 5 sütunlu matrisi girin:
0 0 1 0 0
1 0 0 1 1
0 0 1 0 0
1 0 1 1 1
0 0 0 0 0
"""
