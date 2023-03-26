class Kendaraan:
    def _init_(self, nama):
        self.nama = nama
    def get_nama(self):
        return self.nama
class Mobil(Kendaraan):
    def _init_(self, nama, merek):
        super()._init_(nama)
        self.merek = merek
    def get_merek(self):
        return self.merek
class SepedaMotor(Kendaraan):
    def _init_(self, nama, tipe):
        super()._init_(nama)
        self.tipe = tipe
    def get_tipe(self):
        return self.tipe
# turunan Hierarchical Inheritance
class Truk(Mobil):
    def _init_(self, nama, merek, kapasitas):
        super()._init_(nama, merek)
        self.kapasitas = kapasitas
    def get_kapasitas(self):
        return self.kapasitas
# turunan Hierarchical Inheritance
class MotorListrik(SepedaMotor):
    def _init_(self, nama, tipe, daya):
        super()._init_(nama, tipe)
        self.daya = daya
    def get_daya(self):
        return self.daya