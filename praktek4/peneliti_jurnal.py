class Jurnal :
    def __init__(self, title, date):
        self.title = title
        self.date = date

class Peneliti :
    def __init__(self, nama, jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t: {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t:', jurnal.title)
            print(f'Published\t:', jurnal.date)

jurnal1 = Jurnal('Coronavirus disease 2019: Revies of current literatures', 2020)
jurnal2 = Jurnal('Historical epidemiology of hepatitis C virus (HCV) in select countries-volume3', 2015)
peneliti1 = Peneliti('Evy Yunihastuti', [jurnal1, jurnal2])
jurnal3 = Jurnal('Reverse osmosis applications: Prospect and challenges', 2016)
jurnal4 = Jurnal('Electro-membrane processes for organic acid recovery', 2019)
peneliti2 = Peneliti('Prof. I Gede Wenten', [jurnal3, jurnal4])
peneliti1.daftar_jurnal()
print('='*40)
peneliti2.daftar_jurnal()