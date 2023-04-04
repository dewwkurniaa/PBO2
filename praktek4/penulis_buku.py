class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.inventory = Inventory()
    
    def tampil(self):
        print(f'\nPenulis\t\t: {self.nama}\n')

class Buku:
    def __init__(self, judul, publish, penerbit):
        self.judul = judul
        self.publish = publish
        self.penerbit = penerbit
    
    def get_judul(self):
        return self.judul
    
    def get_publish(self):
        return self.publish
    
    def get_penerbit(self):
        return self.penerbit

class Inventory:
    def __init__(self):
        self.books = []
    
    def add_buku(self, buku):
        self.books.append(buku)

    def daftar_buku(self):
        for buku in self.books:
            print(f'Judul\t\t:', buku.judul)
            print(f'Terbit\t\t:', buku.publish)
            print(f'Penerbitt\t:', buku.penerbit)

penulis1 = Penulis('Habiburrahman El Shirazy')
buku1 = Buku('Ayat-Ayat Cinta', '2003', 'Republika Pesantren Basmala Indonesia')
buku2 = Buku('Ketika Cinta Bertasbih', '2007', 'Republika Basmalah')
buku3 = Buku('Ketika Cinta Berbuah Surga', '2008', 'MQS Publishing')
penulis1.inventory.add_buku(buku1)
penulis1.inventory.add_buku(buku2)
penulis1.inventory.add_buku(buku3)
penulis1.inventory.books
penulis1.tampil()
penulis1.inventory.daftar_buku()