class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def __getitem__(self, product):
        return self.items.get(product, 0)

    def __setitem__(self, product, quantity):
        self.items[product] = quantity

    def display_cart(self):
        print("Shopping Cart:")
        for product, quantity in self.items.items():
            print(f"{product}: {quantity} items")

# Penggunaan
cart = ShoppingCart()

# Menambahkan barang ke keranjang belanja
cart.add_item("Apple", 3)
cart.add_item("Banana", 2)

# Menampilkan keranjang belanja
cart.display_cart()

# Mengakses jumlah barang tertentu menggunakan indeks
apple_quantity = cart["Apple"]
print(f"Jumlah Apple dalam keranjang: {apple_quantity}")

# Mengubah jumlah barang tertentu menggunakan indeks
cart["Banana"] = 5

# Menampilkan keranjang belanja setelah perubahan
cart.display_cart()
