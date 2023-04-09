print('Dewi Kurnia\n210511032\nT121A(R1)\n')

class Kpop:
    def __init__(self,grup,year,fandom):
        self.grup = grup
        self.year = year
        self.fandom = fandom

class Agensi:
    def __init__(self,nama,kpop):
        self.nama = nama
        self.kpop = kpop

    def daftar_kpop(self):
        print(f'\nAgensi\t: {self.nama}\n')
        for kpop in self.kpop:
            print(f'Nama Grup\t: ',kpop.grup)
            print(f'Debut\t\t: {kpop.year}')
            print(f'Nama Fandom\t: {kpop.fandom}')

kpop1 = Kpop('EXO', 2012, "EXO-L")
kpop2 = Kpop('Red Velvet', 2014, "ReVeluv")
kpop3 = Kpop('NCT', 2016, "NCTzen")
kpop4 = Kpop('Aespa', 2020, "My")
agensi1 = Agensi('SM Entertainment', [kpop1, kpop2, kpop3, kpop4])
kpop5 = Kpop('Monsta X', 2019, "Monbebe")
kpop6 = Kpop('IVE', 2021, "Dive")
kpop7 = Kpop('WJSN', 2016, "Ujung")
kpop8 = Kpop('Cravity', 2020, "Luvity")
agensi2 = Agensi('Starship Entertaiment', [kpop5, kpop6, kpop7, kpop8])
agensi1.daftar_kpop()
print('='*40)
agensi2.daftar_kpop()