class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Guru(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip

    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")

guruA = Guru("Bella", 40, "987654321")
guruA.berbicara() 
guruA.mengajar() 