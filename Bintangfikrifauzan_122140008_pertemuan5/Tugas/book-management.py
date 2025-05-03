from abc import ABC, abstractmethod
from datetime import datetime

class LibraryItem(ABC):
    """
    Abstract base class untuk semua item di perpustakaan.
    Menyediakan properti dan method dasar yang akan dimiliki oleh semua item.
    """
    def __init__(self, item_id, title, author, year_published):
        self._item_id = item_id  # protected attribute
        self._title = title  # protected attribute
        self._author = author  # protected attribute
        self._year_published = year_published  # protected attribute
        self._is_available = True  # protected attribute
        self.__borrower = None  # private attribute
        self.__borrow_date = None  # private attribute

    @property
    def item_id(self):
        """Getter untuk ID item."""
        return self._item_id
    
    @property
    def title(self):
        """Getter untuk judul item."""
        return self._title
    
    @property
    def author(self):
        """Getter untuk penulis/pembuat item."""
        return self._author
    
    @property
    def year_published(self):
        """Getter untuk tahun terbit."""
        return self._year_published
    
    @property
    def is_available(self):
        """Getter untuk status ketersediaan item."""
        return self._is_available
    
    def borrow(self, borrower_name):
        """
        Method untuk meminjam item.
        
        Args:
            borrower_name (str): Nama peminjam
        
        Returns:
            bool: True jika peminjaman berhasil, False jika item tidak tersedia
        """
        if self._is_available:
            self._is_available = False
            self.__borrower = borrower_name
            self.__borrow_date = datetime.now()
            return True
        return False
    
    def return_item(self):
        """
        Method untuk mengembalikan item.
        
        Returns:
            tuple: (Nama peminjam, tanggal pinjam) jika pengembalian berhasil
                  None jika item tidak dalam status dipinjam
        """
        if not self._is_available:
            self._is_available = True
            borrower = self.__borrower
            borrow_date = self.__borrow_date
            self.__borrower = None
            self.__borrow_date = None
            return (borrower, borrow_date)
        return None
    
    def get_borrower_info(self):
        """
        Method untuk mendapatkan informasi peminjam.
        
        Returns:
            tuple: (Nama peminjam, tanggal pinjam) jika item dipinjam
                  None jika item tidak dalam status dipinjam
        """
        if not self._is_available and self.__borrower:
            return (self.__borrower, self.__borrow_date)
        return None
    
    @abstractmethod
    def display_details(self):
        """
        Abstract method yang harus diimplementasikan oleh subclass
        untuk menampilkan detail spesifik dari item.
        """
        pass


class Book(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan buku.
    """
    def __init__(self, item_id, title, author, year_published, pages, publisher, isbn):
        super().__init__(item_id, title, author, year_published)
        self.pages = pages
        self.publisher = publisher
        self._isbn = isbn  # protected attribute
    
    @property
    def isbn(self):
        """Getter untuk ISBN buku."""
        return self._isbn
    
    def display_details(self):
        """
        Implementasi method abstract dari parent class.
        Menampilkan detail khusus buku.
        
        Returns:
            str: String berisi detail buku
        """
        availability = "Tersedia" if self._is_available else "Dipinjam"
        details = f"BUKU\n"
        details += f"ID: {self._item_id}\n"
        details += f"Judul: {self._title}\n"
        details += f"Penulis: {self._author}\n"
        details += f"Tahun Terbit: {self._year_published}\n"
        details += f"Halaman: {self.pages}\n"
        details += f"Penerbit: {self.publisher}\n"
        details += f"ISBN: {self._isbn}\n"
        details += f"Status: {availability}"
        
        # Tambahkan info peminjam jika sedang dipinjam
        borrower_info = self.get_borrower_info()
        if borrower_info:
            details += f"\nDipinjam oleh: {borrower_info[0]}"
            details += f"\nTanggal peminjaman: {borrower_info[1].strftime('%d-%m-%Y %H:%M')}"
        
        return details


class Magazine(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan majalah.
    """
    def __init__(self, item_id, title, publisher, year_published, issue_number, month):
        super().__init__(item_id, title, publisher, year_published)
        self.issue_number = issue_number
        self.month = month
    
    def display_details(self):
        """
        Implementasi method abstract dari parent class.
        Menampilkan detail khusus majalah.
        
        Returns:
            str: String berisi detail majalah
        """
        availability = "Tersedia" if self._is_available else "Dipinjam"
        details = f"MAJALAH\n"
        details += f"ID: {self._item_id}\n"
        details += f"Judul: {self._title}\n"
        details += f"Penerbit: {self._author}\n"  # Dalam kasus majalah, author digunakan sebagai penerbit
        details += f"Tahun Terbit: {self._year_published}\n"
        details += f"Nomor Edisi: {self.issue_number}\n"
        details += f"Bulan: {self.month}\n"
        details += f"Status: {availability}"
        
        # Tambahkan info peminjam jika sedang dipinjam
        borrower_info = self.get_borrower_info()
        if borrower_info:
            details += f"\nDipinjam oleh: {borrower_info[0]}"
            details += f"\nTanggal peminjaman: {borrower_info[1].strftime('%d-%m-%Y %H:%M')}"
        
        return details


class DVD(LibraryItem):
    """
    Subclass tambahan dari LibraryItem yang merepresentasikan DVD.
    """
    def __init__(self, item_id, title, director, year_published, duration, genre):
        super().__init__(item_id, title, director, year_published)
        self.duration = duration  # dalam menit
        self.genre = genre
    
    def display_details(self):
        """
        Implementasi method abstract dari parent class.
        Menampilkan detail khusus DVD.
        
        Returns:
            str: String berisi detail DVD
        """
        availability = "Tersedia" if self._is_available else "Dipinjam"
        details = f"DVD\n"
        details += f"ID: {self._item_id}\n"
        details += f"Judul: {self._title}\n"
        details += f"Sutradara: {self._author}\n"  # Dalam kasus DVD, author digunakan sebagai sutradara
        details += f"Tahun Terbit: {self._year_published}\n"
        details += f"Durasi: {self.duration} menit\n"
        details += f"Genre: {self.genre}\n"
        details += f"Status: {availability}"
        
        # Tambahkan info peminjam jika sedang dipinjam
        borrower_info = self.get_borrower_info()
        if borrower_info:
            details += f"\nDipinjam oleh: {borrower_info[0]}"
            details += f"\nTanggal peminjaman: {borrower_info[1].strftime('%d-%m-%Y %H:%M')}"
        
        return details


class Library:
    """
    Class untuk menyimpan dan mengelola koleksi item perpustakaan.
    """
    def __init__(self, name):
        self.name = name
        self.__items = {}  # private attribute untuk menyimpan semua item
    
    @property
    def item_count(self):
        """
        Property decorator untuk menghitung jumlah item di perpustakaan.
        
        Returns:
            int: Jumlah item di perpustakaan
        """
        return len(self.__items)
    
    def add_item(self, item):
        """
        Method untuk menambahkan item ke perpustakaan.
        
        Args:
            item (LibraryItem): Item yang akan ditambahkan (harus subclass dari LibraryItem)
        
        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada atau bukan LibraryItem)
        """
        if not isinstance(item, LibraryItem):
            print("Error: Item harus merupakan jenis LibraryItem")
            return False
        
        if item.item_id in self.__items:
            print(f"Error: Item dengan ID {item.item_id} sudah ada di perpustakaan")
            return False
        
        self.__items[item.item_id] = item
        return True
    
    def remove_item(self, item_id):
        """
        Method untuk menghapus item dari perpustakaan berdasarkan ID.
        
        Args:
            item_id (str): ID item yang akan dihapus
        
        Returns:
            LibraryItem: Item yang dihapus, atau None jika tidak ditemukan
        """
        if item_id in self.__items:
            return self.__items.pop(item_id)
        return None
    
    def find_item_by_id(self, item_id):
        """
        Method untuk mencari item berdasarkan ID.
        
        Args:
            item_id (str): ID item yang dicari
        
        Returns:
            LibraryItem: Item yang ditemukan, atau None jika tidak ditemukan
        """
        return self.__items.get(item_id)
    
    def find_items_by_title(self, title):
        """
        Method untuk mencari item berdasarkan judul (pencarian parsial).
        
        Args:
            title (str): Judul atau bagian judul yang dicari
        
        Returns:
            list: Daftar item yang judulnya mengandung parameter title
        """
        return [item for item in self.__items.values() 
                if title.lower() in item.title.lower()]
    
    def list_all_items(self):
        """
        Method untuk mendapatkan semua item di perpustakaan.
        
        Returns:
            list: Daftar semua item di perpustakaan
        """
        return list(self.__items.values())
    
    def list_available_items(self):
        """
        Method untuk mendapatkan semua item yang tersedia untuk dipinjam.
        
        Returns:
            list: Daftar item yang tersedia
        """
        return [item for item in self.__items.values() if item.is_available]
    
    def list_borrowed_items(self):
        """
        Method untuk mendapatkan semua item yang sedang dipinjam.
        
        Returns:
            list: Daftar item yang sedang dipinjam
        """
        return [item for item in self.__items.values() if not item.is_available]


# Fungsi untuk menu interaktif
def main():
    # Membuat perpustakaan baru
    nama_perpus = input("Masukkan nama perpustakaan: ")
    perpus = Library(nama_perpus)
    
    # Menambahkan beberapa item contoh untuk demo
    tambah_item_contoh(perpus)
    
    while True:
        print("\n" + "="*50)
        print(f"SISTEM MANAJEMEN PERPUSTAKAAN - {perpus.name}")
        print("="*50)
        print("1. Tambah Item Baru")
        print("2. Cari Item berdasarkan ID")
        print("3. Cari Item berdasarkan Judul")
        print("4. Tampilkan Semua Item")
        print("5. Tampilkan Item yang Tersedia")
        print("6. Tampilkan Item yang Dipinjam")
        print("7. Pinjam Item")
        print("8. Kembalikan Item")
        print("9. Hapus Item")
        print("0. Keluar")
        
        pilihan = input("\nPilih menu (0-9): ")
        
        if pilihan == "1":
            tambah_item_baru(perpus)
        elif pilihan == "2":
            cari_item_by_id(perpus)
        elif pilihan == "3":
            cari_item_by_title(perpus)
        elif pilihan == "4":
            tampilkan_semua_item(perpus)
        elif pilihan == "5":
            tampilkan_item_tersedia(perpus)
        elif pilihan == "6":
            tampilkan_item_dipinjam(perpus)
        elif pilihan == "7":
            pinjam_item(perpus)
        elif pilihan == "8":
            kembalikan_item(perpus)
        elif pilihan == "9":
            hapus_item(perpus)
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan Sistem Manajemen Perpustakaan!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            
        input("\nTekan Enter untuk melanjutkan...")


def tambah_item_contoh(perpus):
    """Menambahkan beberapa item contoh ke perpustakaan"""
    # Menambahkan beberapa buku
    buku1 = Book("B001", "Python Programming", "John Smith", 2020, 450, "Packt Publishing", "978-1234567890")
    buku2 = Book("B002", "Data Science with Python", "Jane Doe", 2021, 380, "O'Reilly", "978-0987654321")
    buku3 = Book("B003", "Object-Oriented Programming", "Bob Johnson", 2019, 320, "Manning", "978-5678901234")
    
    # Menambahkan beberapa majalah
    majalah1 = Magazine("M001", "National Geographic", "National Geographic Society", 2022, 256, "January")
    majalah2 = Magazine("M002", "Tech Magazine", "Tech Media Inc", 2022, 48, "February")
    
    # Menambahkan DVD
    dvd1 = DVD("D001", "Python Tutorial Series", "Code Academy", 2021, 180, "Educational")
    
    # Menambahkan item ke perpustakaan
    items = [buku1, buku2, buku3, majalah1, majalah2, dvd1]
    for item in items:
        perpus.add_item(item)
    
    print(f"Item contoh telah ditambahkan ke {perpus.name}. Total: {perpus.item_count} item")


def tambah_item_baru(perpus):
    """Fungsi untuk menambahkan item baru ke perpustakaan"""
    print("\nTAMBAH ITEM BARU")
    print("-"*40)
    print("Pilih jenis item:")
    print("1. Buku")
    print("2. Majalah")
    print("3. DVD")
    
    jenis = input("Pilih jenis item (1-3): ")
    
    if jenis not in ["1", "2", "3"]:
        print("Pilihan tidak valid!")
        return
    
    # Input data umum
    item_id = input("Masukkan ID Item: ")
    title = input("Masukkan Judul: ")
    year_published = input("Masukkan Tahun Terbit: ")
    
    try:
        year_published = int(year_published)
    except ValueError:
        print("Tahun harus berupa angka!")
        return
    
    if jenis == "1":  # Buku
        author = input("Masukkan Nama Penulis: ")
        pages = input("Masukkan Jumlah Halaman: ")
        publisher = input("Masukkan Nama Penerbit: ")
        isbn = input("Masukkan ISBN: ")
        
        try:
            pages = int(pages)
        except ValueError:
            print("Jumlah halaman harus berupa angka!")
            return
        
        new_item = Book(item_id, title, author, year_published, pages, publisher, isbn)
    
    elif jenis == "2":  # Majalah
        publisher = input("Masukkan Nama Penerbit: ")
        issue_number = input("Masukkan Nomor Edisi: ")
        month = input("Masukkan Bulan Terbit: ")
        
        try:
            issue_number = int(issue_number)
        except ValueError:
            print("Nomor edisi harus berupa angka!")
            return
        
        new_item = Magazine(item_id, title, publisher, year_published, issue_number, month)
    
    elif jenis == "3":  # DVD
        director = input("Masukkan Nama Sutradara/Pembuat: ")
        duration = input("Masukkan Durasi (menit): ")
        genre = input("Masukkan Genre: ")
        
        try:
            duration = int(duration)
        except ValueError:
            print("Durasi harus berupa angka!")
            return
        
        new_item = DVD(item_id, title, director, year_published, duration, genre)
    
    # Tambahkan item baru ke perpustakaan
    if perpus.add_item(new_item):
        print(f"Item baru berhasil ditambahkan! ID: {item_id}")
    else:
        print("Gagal menambahkan item.")


def cari_item_by_id(perpus):
    """Fungsi untuk mencari item berdasarkan ID"""
    print("\nCARI ITEM BERDASARKAN ID")
    print("-"*40)
    
    item_id = input("Masukkan ID item yang dicari: ")
    item = perpus.find_item_by_id(item_id)
    
    if item:
        print("\nItem ditemukan!\n")
        print(item.display_details())
    else:
        print(f"Item dengan ID '{item_id}' tidak ditemukan.")


def cari_item_by_title(perpus):
    """Fungsi untuk mencari item berdasarkan judul"""
    print("\nCARI ITEM BERDASARKAN JUDUL")
    print("-"*40)
    
    title = input("Masukkan kata kunci judul: ")
    items = perpus.find_items_by_title(title)
    
    if items:
        print(f"\nDitemukan {len(items)} item dengan kata kunci '{title}':")
        for idx, item in enumerate(items, 1):
            print(f"\n{idx}. {item.title} (ID: {item.item_id})")
            print("   " + "-"*30)
            print("   " + "\n   ".join(item.display_details().split("\n")))
    else:
        print(f"Tidak ditemukan item dengan judul mengandung '{title}'.")


def tampilkan_semua_item(perpus):
    """Fungsi untuk menampilkan semua item dalam perpustakaan"""
    print("\nDAFTAR SEMUA ITEM")
    print("-"*40)
    
    items = perpus.list_all_items()
    
    if items:
        print(f"Total: {len(items)} item\n")
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item.title} (ID: {item.item_id}) - {'Tersedia' if item.is_available else 'Dipinjam'}")
    else:
        print("Perpustakaan kosong. Tidak ada item untuk ditampilkan.")


def tampilkan_item_tersedia(perpus):
    """Fungsi untuk menampilkan item yang tersedia"""
    print("\nDAFTAR ITEM TERSEDIA")
    print("-"*40)
    
    items = perpus.list_available_items()
    
    if items:
        print(f"Total: {len(items)} item tersedia\n")
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item.title} (ID: {item.item_id})")
    else:
        print("Tidak ada item yang tersedia untuk dipinjam.")


def tampilkan_item_dipinjam(perpus):
    """Fungsi untuk menampilkan item yang dipinjam"""
    print("\nDAFTAR ITEM DIPINJAM")
    print("-"*40)
    
    items = perpus.list_borrowed_items()
    
    if items:
        print(f"Total: {len(items)} item dipinjam\n")
        for idx, item in enumerate(items, 1):
            borrower_info = item.get_borrower_info()
            print(f"{idx}. {item.title} (ID: {item.item_id})")
            print(f"   Dipinjam oleh: {borrower_info[0]}")
            print(f"   Tanggal: {borrower_info[1].strftime('%d-%m-%Y %H:%M')}")
    else:
        print("Tidak ada item yang sedang dipinjam.")


def pinjam_item(perpus):
    """Fungsi untuk meminjam item"""
    print("\nPINJAM ITEM")
    print("-"*40)
    
    item_id = input("Masukkan ID item yang ingin dipinjam: ")
    item = perpus.find_item_by_id(item_id)
    
    if not item:
        print(f"Item dengan ID '{item_id}' tidak ditemukan.")
        return
    
    if not item.is_available:
        print(f"Item '{item.title}' sedang dipinjam dan tidak tersedia.")
        return
    
    borrower_name = input("Masukkan nama peminjam: ")
    
    if item.borrow(borrower_name):
        print(f"Item '{item.title}' berhasil dipinjam oleh {borrower_name}.")
    else:
        print("Gagal meminjam item.")


def kembalikan_item(perpus):
    """Fungsi untuk mengembalikan item"""
    print("\nKEMBALIKAN ITEM")
    print("-"*40)
    
    item_id = input("Masukkan ID item yang ingin dikembalikan: ")
    item = perpus.find_item_by_id(item_id)
    
    if not item:
        print(f"Item dengan ID '{item_id}' tidak ditemukan.")
        return
    
    if item.is_available:
        print(f"Item '{item.title}' tidak dalam status dipinjam.")
        return
    
    return_info = item.return_item()
    if return_info:
        print(f"Item '{item.title}' berhasil dikembalikan.")
        print(f"Sebelumnya dipinjam oleh: {return_info[0]}")
        print(f"Tanggal peminjaman: {return_info[1].strftime('%d-%m-%Y %H:%M')}")
    else:
        print("Gagal mengembalikan item.")


def hapus_item(perpus):
    """Fungsi untuk menghapus item dari perpustakaan"""
    print("\nHAPUS ITEM")
    print("-"*40)
    
    item_id = input("Masukkan ID item yang ingin dihapus: ")
    item = perpus.remove_item(item_id)
    
    if item:
        print(f"Item '{item.title}' (ID: {item.item_id}) berhasil dihapus dari perpustakaan.")
    else:
        print(f"Item dengan ID '{item_id}' tidak ditemukan.")


if __name__ == "__main__":
    main()