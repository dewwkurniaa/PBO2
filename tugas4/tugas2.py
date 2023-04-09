print('Dewi Kurnia\n210511032\nT121A(R1)\n')

class judul_lagu:
    def __init__(self,judul=None):
        if judul is None:
            self.judul = []
        else:
            self.judul = judul

    def add_judul(self,judul):
        self.judul.append(judul)

    def daftar_judul(self):
        for judul in self.judul:
            print(f'Judul\t\t: ',judul.judul)
            print(f'Album\t\t: ',judul.album)
            print(f'Tahun Rilis\t: ',judul.thn_rilis)

class Judul:
    def __init__(self,judul,album,thn_rilis):
        self.judul = judul
        self.album = album
        self.thn_rilis = thn_rilis

    def get_thn_rilis(self):
        return self.thn_rilis

    def get_album(self):
        return self.album
    
    def get_thn_rilis(self):
        return self.thn_rilis

class Lagu:
    def __init__(self,name_lagu,judul_lagu):
        self.name_lagu = name_lagu
        self.judul_lagu = judul_lagu

    def tampil(self):
        print(f'\nPenyanyi\t: {self.name_lagu}\n')

judul1 = Judul('MAMA', 'MAMA', 2012)
judul2 = Judul('Wolf', 'XOXO', 2013)
judul3 = Judul('Overdose', 'Overdose', 2014)
judul4 = Judul('Call Me Baby', 'EXODUS', 2015)
judul5 = Judul('Lucky One', 'EX-ACT', 2016)
judul6 = Judul('Ko Ko Bop', 'The Eve', 2017)
judul7 = Judul('Tempo', 'Dont Mess Up My Tempo', 2018)
judul8 = Judul('Obsession', 'Obsession', 2019)
judul9 = Judul('Runaway', 'Dont Fight The Feeling', 2021)
judul_lagu = judul_lagu([judul1, judul2, judul3, judul4, judul5, judul6, judul7, judul8, judul9])
lagu = Lagu('EXO', judul_lagu)
lagu.judul_lagu.judul
lagu.tampil()
print("="*40)
lagu.judul_lagu.daftar_judul()