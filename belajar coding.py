# inventory.py
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} | Stok: {self.quantity} | Harga: Rp{self.price:,}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = Item(name, quantity, price)
        self.items.append(item)
        print(f"[+] {name} berhasil ditambahkan.")

    def view_items(self):
        if not self.items:
            print("Inventaris kosong.")
            return
        print("\n=== Daftar Inventaris ===")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item}")

    def update_item(self, index, quantity=None, price=None):
        try:
            item = self.items[index - 1]
            if quantity is not None:
                item.quantity = quantity
            if price is not None:
                item.price = price
            print(f"[✓] Data {item.name} berhasil diperbarui.")
        except IndexError:
            print("[!] Item tidak ditemukan.")

    def delete_item(self, index):
        try:
            item = self.items.pop(index - 1)
            print(f"[-] {item.name} berhasil dihapus.")
        except IndexError:
            print("[!] Item tidak ditemukan.")

    def save_to_file(self, filename="data.txt"):
        with open(filename, "w") as f:
            for item in self.items:
                f.write(f"{item.name},{item.quantity},{item.price}\n")
        print("[💾] Data berhasil disimpan.")

    def load_from_file(self, filename="data.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, qty, price = line.strip().split(",")
                    self.add_item(name, int(qty), float(price))
            print("[📂] Data berhasil dimuat.")
        except FileNotFoundError:
            print("[!] File data tidak ditemukan. Memulai dengan inventaris kosong.")
