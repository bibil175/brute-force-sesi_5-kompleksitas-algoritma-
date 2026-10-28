from itertools import permutations
 
# Daftar simpul (titik) yang akan dikunjungi
simpul = ['A', 'B', 'C', 'D', 'E', 'F']
 
# Waktu tempuh antar simpul (dalam menit)
waktu = {
    ('A', 'B'): 12, ('A', 'C'): 10, ('A', 'D'): 19,
    ('A', 'E'): 8,  ('A', 'F'): 15, ('B', 'C'): 3,
    ('B', 'D'): 7,  ('B', 'E'): 6,  ('B', 'F'): 9,
    ('C', 'D'): 11, ('C', 'E'): 14, ('C', 'F'): 5,
    ('D', 'E'): 4,  ('D', 'F'): 13, ('E', 'F'): 16,
}
 
def ambil_waktu(x, y):
    # Jalur bisa dilewati dua arah, jadi cek kedua urutan
    if (x, y) in waktu:
        return waktu[(x, y)]
    return waktu[(y, x)]
 
semua_rute = []
sudah_ada = set()
 
# Simpul A dijadikan titik awal, simpul lainnya diacak urutannya
for urutan in permutations(simpul[1:]):
    # Lewati rute yang hanya merupakan kebalikan dari rute sebelumnya
    kunci = min(urutan, urutan[::-1])
    if kunci in sudah_ada:
        continue
    sudah_ada.add(kunci)
 
    rute = ['A'] + list(urutan) + ['A']
    total = 0
    for i in range(len(rute) - 1):
        total += ambil_waktu(rute[i], rute[i + 1])
    semua_rute.append((total, rute))
 
# Urutkan dari waktu paling singkat
semua_rute.sort()
 
print("Jumlah rute unik :", len(semua_rute))
print("Rute tercepat    :", " - ".join(semua_rute[0][1]))
print("Total waktu      :", semua_rute[0][0], "menit")
terlama = semua_rute[-1]
print("Rute terlama     :", " - ".join(terlama[1]), "(", terlama[0], "menit )")
