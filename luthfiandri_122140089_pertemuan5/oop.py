from abc import ABC, abstractmethod

# Abstract class untuk item perpustakaan
# Menjadi dasar bagi semua jenis item seperti buku dan majalah
class LibraryItem(ABC):
    def __init__(self, item_id, title, publisher):
        self._item_id = item_id     # Protected: ID item
        self._title = title         # Protected: Judul item
        self._publisher = publisher # Penerbit item

    @abstractmethod
    def display_info(self):
        # Method abstrak: harus diimplementasikan oleh subclass
        pass

    @property
    def title(self):
        # Property untuk mengakses judul item
        return self._title

    @property
    def item_id(self):
        # Property untuk mengakses ID item
        return self._item_id


# Subclass Book, mewarisi LibraryItem
# Mewakili item berupa buku
class Book(LibraryItem):
    def __init__(self, item_id, title, publisher, author, num_pages):
        super().__init__(item_id, title, publisher)
        self._author = author        # Penulis buku
        self._num_pages = num_pages  # Jumlah halaman

    def display_info(self):
        # Implementasi method abstrak untuk menampilkan info buku
        print(f"[Book] ID: {self._item_id}, Title: {self._title}, Author: {self._author}, Pages: {self._num_pages}, Publisher: {self._publisher}")


# Subclass Magazine, mewarisi LibraryItem
# Mewakili item berupa majalah
class Magazine(LibraryItem):
    def __init__(self, item_id, title, publisher, issue_number):
        super().__init__(item_id, title, publisher)
        self._issue_number = issue_number  # Nomor edisi majalah

    def display_info(self):
        # Implementasi method abstrak untuk menampilkan info majalah
        print(f"[Magazine] ID: {self._item_id}, Title: {self._title}, Issue: {self._issue_number}, Publisher: {self._publisher}")


# Class Library: menyimpan dan mengelola koleksi item
class Library:
    def __init__(self):
        self.__collection = []  # Private: daftar item perpustakaan

    def add_item(self, item: LibraryItem):
        # Menambahkan item baru ke koleksi
        self.__collection.append(item)
        print(f"Item '{item.title}' berhasil ditambahkan.")

    def display_all_items(self):
        # Menampilkan semua item yang ada di perpustakaan
        if not self.__collection:
            print("Perpustakaan kosong.")
            return
        print("Daftar Koleksi:")
        for item in self.__collection:
            item.display_info()

    def find_item_by_title(self, title):
        # Mencari item berdasarkan judul
        found = [item for item in self.__collection if item.title.lower() == title.lower()]
        if found:
            for item in found:
                item.display_info()
        else:
            print("Item tidak ditemukan.")

    def find_item_by_id(self, item_id):
        # Mencari item berdasarkan ID
        for item in self.__collection:
            if item.item_id == item_id:
                item.display_info()
                return
        print("Item tidak ditemukan.")


# Fungsi utama untuk interaksi dengan pengguna
def main():
    library = Library()
    
    while True:
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah Item")
        print("2. Lihat Semua Item")
        print("3. Cari Berdasarkan Judul")
        print("4. Cari Berdasarkan ID")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            # Menambahkan item baru
            item_type = input("Jenis item (book/magazine): ").lower()
            item_id = input("ID: ")
            title = input("Judul: ")
            publisher = input("Penerbit: ")

            if item_type == 'book':
                # Tambah buku
                author = input("Penulis: ")
                num_pages = input("Jumlah halaman: ")
                book = Book(item_id, title, publisher, author, num_pages)
                library.add_item(book)
            elif item_type == 'magazine':
                # Tambah majalah
                issue = input("Nomor edisi: ")
                magazine = Magazine(item_id, title, publisher, issue)
                library.add_item(magazine)
            else:
                print("Jenis item tidak dikenal.")

        elif choice == '2':
            # Menampilkan semua item
            library.display_all_items()

        elif choice == '3':
            # Mencari item berdasarkan judul
            title = input("Masukkan judul yang dicari: ")
            library.find_item_by_title(title)

        elif choice == '4':
            # Mencari item berdasarkan ID
            item_id = input("Masukkan ID yang dicari: ")
            library.find_item_by_id(item_id)

        elif choice == '5':
            # Keluar dari program
            print("Keluar dari sistem. Sampai jumpa!")
            break

        else:
            # Input tidak valid
            print("Pilihan tidak valid. Silakan coba lagi.")

# Eksekusi program
if __name__ == "__main__":
    main()
