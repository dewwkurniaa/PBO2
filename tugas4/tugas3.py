print('Dewi Kurnia\n210511032\nT121A(R1)\n')

class Nama_Member:
    def __init__(self,nama=None):
        if nama is None:
            self.nama = []
        else:
            self.nama = nama

    def add_nama(self,nama):
        self.nama.append(nama)

    def daftar_nama(self):
        for nama in self.nama:
            print(f'Nama\t\t: ',nama.nama)
            print(f'Umur\t\t: ',nama.genre)
            print(f'Posisi\t\t: ',nama.tgl_rilis)

class Nama:
    def __init__(self,nama,genre,tgl_rilis):
        self.nama = nama
        self.genre = genre
        self.tgl_rilis = tgl_rilis

    def get_tgl_rilis(self):
        return self.tgl_rilis

    def get_genre(self):
        return self.genre
    
    def get_tgl_rilis(self):
        return self.tgl_rilis

class Member:
    def __init__(self,name_member,nama_member):
        self.name_member = name_member
        self.nama_member = nama_member

    def tampil(self):
        print(f'\nNama Grup\t: {self.name_member}\n')

nama1 = Nama('Kim Minsoek', 33, "Lead Vocal, Sub Rapper")
nama2 = Nama('Kim Junmyoen', 31, "Leader, Lead Vocal, Visual")
nama3 = Nama('Zhang Yixing', 31, "Main Dancer, Sub Vocal, Sub Rapper")
nama4 = Nama('Byun Baekhyun', 30, "Main Vocal")
nama5 = Nama('Kim Jongdae', 30, "Main Vocal")
nama6 = Nama('Park Chanyeol', 30, "Main Rapper, Sub Vocal, Visual")
nama7 = Nama('D.O. Kyungsoo', 30, "Main Vocal")
nama8 = Nama('Kim Jong-in', 29, "Main Dancer, Lead Rapper, Sub Vocalist, Center, Visual")
nama9 = Nama('Ooh Sehun', 29, "Lead Dancer, Lead Rapper, Visual, Maknae")
nama_member = Nama_Member([nama1, nama2, nama3, nama4, nama5, nama6, nama7, nama8, nama9])
member = Member('EXO', nama_member)
member.nama_member.nama
member.tampil()
print("="*40)
member.nama_member.daftar_nama()