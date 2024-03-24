class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.dipinjam = False
        
    def pinjam(self):
        if not self.dipinjam:
            print(f'Buku {self.judul} berhasil dipinjam.')
            self.dipinjam = True
        else:
            print(f'buku {self.judul} sudah dipinjam')
    
    def kebalikan(self):
        if self.dipinjam:
            print(f'buku {self.judul} dikembalikan.')
            self.dipinjam = False
        else: 
            print(f'buku {self.judul} belum dipinjam.')
            
            
    def info(self):
        status = "dipinjam" if self.dipinjam else "Tersedia"
        print(f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}, Status: {status}")


buku1 = Buku("tutorial python","Abdi", 2009)
buku2 = Buku("tutorial OOP di python", "Kiki", 2014)

print("informasi sebelum dipinjam:")
buku1.info()
buku2.info()

# meminjam dan mengembalikan buku
buku1.pinjam()

buku1.info()

