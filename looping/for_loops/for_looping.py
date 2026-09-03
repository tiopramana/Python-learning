# for loops = For loops adalah salah satu cara untuk melakukan perulangan (iterasi) dalam pemrograman.
#       Berdasarkan tipe data string, list, tuple, set, dan dictionary.

#for item in collection:
    # kode yang akan dijalankan berulang

# for x in range(1, 5):
#     if x == 3:
#         continue
#     else:
#         print(x)




# for i in range(1, 5 + 1):
#     spaces = " " * (5 - i)
#     hashes = "*" * (2 * i - 1)
#     print(spaces + hashes)

class Kalkulator:
    pajak = 0.1  # Class Variable

    def __init__(self, nama):
        self.nama = nama

    @staticmethod
    def hitung_diskon(harga, persen):
        return harga * (persen / 100)

    def hitung_total(self, harga):
        return harga + (harga * self.pajak)


class KalkulatorPremium(Kalkulator):
    pajak = 0.05  # Class Variable Overriding


# Eksekusi Kode
k1 = Kalkulator("Standard")
k2 = KalkulatorPremium("Premium")

print(k1.hitung_diskon(100000, 10))
print(k2.hitung_total(100000))
