class LibraryStack:
    def __init__(self):
        self.books = []

    def is_empty(self):
        return len(self.books) == 0

    def add_book(self, book):
        self.books.append(book)
        print(f"Buku '{book}' berhasil ditambahkan ke perpustakaan.")

    def remove_book(self):
        if not self.is_empty():
            removed_book = self.books.pop()
            print(f"Buku '{removed_book}' berhasil dihapus dari perpustakaan.")
        else:
            print("Perpustakaan kosong. Tidak ada buku yang dapat dihapus.")

    def view_books(self):
        if not self.is_empty():
            print("Daftar Buku di Perpustakaan:")
            for book in reversed(self.books):
                print(f"- {book}")
        else:
            print("Perpustakaan kosong.")

def main():
    library = LibraryStack()

    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambahkan Buku")
        print("2. Hapus Buku Terbaru")
        print("3. Lihat Daftar Buku")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == '1':
            book_title = input("Masukkan judul buku: ")
            library.add_book(book_title)
        elif choice == '2':
            library.remove_book()
        elif choice == '3':
            library.view_books()
        elif choice == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
