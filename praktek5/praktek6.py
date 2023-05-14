print('Dewi Kurnia\n210511032\nT121A(R1)\n')

class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

hewan = Hewan("Kucing", 5)

try:
    print(hewan.jenis)

except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")