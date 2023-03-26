class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def belajar(self):
        print(self.nama, "sedang belajar")

class DriverGojek:
    def __init__(self, nama, drivergojek):
        self.nama = nama
        self.drivergojek = drivergojek

    def bekerja(self):
        print(self.nama, "sedang mengantar penumpang")

class MahasiswaDriverGojek(Mahasiswa, DriverGojek):
    def __init__(self, nama, nim, drivergojek):
        Mahasiswa.__init__(self, nama, nim)
        DriverGojek.__init__(self, nama, drivergojek)

    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")

mhs_drivergojek = MahasiswaDriverGojek("Dewi", "210511032", "Driver Gojek")
mhs_drivergojek.belajar() # output: Dewi sedang belajar
mhs_drivergojek.bekerja() # output: Dewi sedang mengantar penumpang
mhs_drivergojek.bersosialisasi() # output: Dewi sedang bersosialisasi