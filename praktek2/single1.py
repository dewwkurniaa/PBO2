class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "bergerak")

class Ayam(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("Kukkuk")
        
ayamA = Ayam("Ayam Jago", 1, "Kukkuk")
ayamA.bergerak() 
ayamA.bersuara() 