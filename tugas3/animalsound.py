from playsound import playsound

class hewan:
    def __init__(self,hewan):
        self.hewan = hewan
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')

class anjing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_anjing.mp3")

class ayam(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_ayam.mp3")

class babi(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_babi.mp3")

class elang(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_elang.mp3")

class gajah(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_gajah.mp3")

class kambing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_kambing.mp3")

class kucing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_kucing.mp3")

class kuda(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_kuda.mp3")

class macan(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_macan.mp3")

class nyamuk(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\PBO2\pert3\Tugas\suara hewan_nyamuk.mp3")

def hewan_bersuara(hewan):
    hewan.bersuara()

hewan0 = hewan('Hewan')
hewan1 = anjing('Anjing')
hewan2 = ayam('Ayam')
hewan3 = babi('Babi')
hewan4 = elang('Elang')
hewan5 = gajah('Gajah')
hewan6 = kambing('Kambing')
hewan7 = kucing('Kucing')
hewan8 = kuda('Kuda')
hewan9 = macan('Macan')
hewan10 = nyamuk('Nyamuk')

hewan_bersuara(hewan0)
hewan_bersuara(hewan1)
hewan_bersuara(hewan2)
hewan_bersuara(hewan3)
hewan_bersuara(hewan4)
hewan_bersuara(hewan5)
hewan_bersuara(hewan6)
hewan_bersuara(hewan7)
hewan_bersuara(hewan8)
hewan_bersuara(hewan9)
hewan_bersuara(hewan10)