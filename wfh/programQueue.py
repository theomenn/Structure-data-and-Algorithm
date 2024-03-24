import os

class MyQueue:
    def __init__(self, max_length):
        self.items = []
        self.max_length = max_length

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_length

    def enqueue(self, item):
        if not self.is_full():
            self.items.append(item)
            print(f"Elemen {item} berhasil ditambahkan ke dalam queue.")
        else:
            print("Queue sudah penuh. Tidak dapat menambahkan elemen.")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. No front element.")
    def AllItems(self):
        if not self.is_empty():
            return self.items
        else:
            print("Queue is empty. No Element.")

    def size(self):
        return len(self.items)

# Interaksi pengguna
def main():
    # Meminta panjang queue dari pengguna
    panjang_queue = int(input("Masukkan panjang queue: "))
    queue = MyQueue(panjang_queue)

    while True:
        # Membersihkan layar konsol
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\nMenu:")
        print("1. Enqueue (Tambah elemen)")
        print("2. Dequeue (Hapus elemen)")
        print("3. Lihat elemen pertama")
        print("4. Lihat ukuran queue")
        print("5. Lihat seluruh elemen")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

        if pilihan == '1':
            elemen = input("Masukkan elemen yang akan ditambahkan: ")
            queue.enqueue(elemen)
        elif pilihan == '2':
            dequeued_element = queue.dequeue()
            if dequeued_element is not None:
                print(f"Elemen {dequeued_element} dihapus dari queue.")
        elif pilihan == '3':
            print("Elemen pertama dalam queue:", queue.front())
        elif pilihan == '4':
            print("Ukuran queue:", queue.size())
        elif pilihan == '5':
            print("semua elemen:", queue.AllItems())
        elif pilihan == '6':
            os.system('cls')
            print("Terima Kasih telah menggunakan program kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        # Tunggu pengguna menekan Enter sebelum membersihkan layar dan kembali ke menu
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()


