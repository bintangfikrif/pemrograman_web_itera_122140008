# Tracker Keuangan Mahasiswa

## Deskripsi
Student Financial Tracker adalah aplikasi web yang dirancang untuk membantu mahasiswa 
mengelola keuangan pribadi mereka dengan mudah. Aplikasi ini memungkinkan pengguna untuk mencatat pemasukan dan 
pengeluaran, mengatur budget bulanan, serta melihat visualisasi keuangan mereka dalam bentuk grafik untuk memantau 
kebiasaan pengeluaran

## Fitur Utama
- Pencatatan Transaksi: Tambahkan pemasukan dan pengeluaran dengan detail kategori dan deskripsi
- Saldo Realtime: Lihat jumlah saldo saat ini yang diperbarui secara otomatis
- Pengaturan Budget: Tetapkan budget bulanan dan lihat progress penggunaan budget
- Visualisasi Data: Lihat grafik pemasukan dan pengeluaran bulanan
- Riwayat Transaksi: Cari dan kelola riwayat transaksi yang sudah direkam
- Penyimpanan Lokal: Data tersimpan di browser sehingga tidak hilang ketika halaman direfresh

## Screenshoot Tampilan Aplikasi
1. Overview Aplikasi
![image](https://github.com/user-attachments/assets/994cb68e-be6b-4672-9247-fe531e642002)
![image](https://github.com/user-attachments/assets/b60d80a1-9bed-43c9-8b2d-ab04cb01bc91)

2. Fitur Saldo Realtime & Penambahan Transaksi
![image](https://github.com/user-attachments/assets/cb7624fb-d64d-47d1-be53-44475ef74ad7)

3. Fitur Pengaturan Budget Bulanan
![image](https://github.com/user-attachments/assets/d3b6f8dc-8bcc-4cdb-bf9e-c0e703fc48a6)

4. Fitur Visualisasi Keuangan
![image](https://github.com/user-attachments/assets/6cb9e003-ce1d-49c3-a12e-11468f7858ff)

5. Fitur Riwayat Transaksi
![image](https://github.com/user-attachments/assets/43c6310f-22f5-430d-bf37-4952f05fa8d2)
  

## Teknologi & Implementasi ES6+
Aplikasi ini mengimplementasikan berbagai fitur ES6+ modern seperti:
1. *Class & OOP*. Menggunakan class Transaction dan FinancialTracker untuk organisasi kode yang lebih baik.
   ```sh
   class Transaction {
    constructor(id, amount, description, category, type, date) {
        this.id = id;
        this.amount = amount;
        // ...
    }
    
    get formattedAmount() {
        return new Intl.NumberFormat('id-ID', { 
            style: 'currency', 
            currency: 'IDR',
            // ...
        }).format(this.amount);
    }
   }
   ```
2. *Getter Methods*. Untuk formatting nilai mata uang dan tanggal.
   ```sh
   get formattedDate() {
    return new Date(this.date).toLocaleDateString('id-ID', {
        year: 'numeric',
        month: 'short',
        // ...
    });
   }
   ```
3. *Arrow Functions*. Untuk callback functions yang lebih singkat dan jelas.
   ```sh
   deleteBtn.addEventListener('click', () => this.deleteTransaction(transaction.id));
   ```
4. *Template Literals*. Untuk pembuatan elemen HTML yang dinamis.
   ```sh
   transactionElement.innerHTML = `
      <div class="transaction-date">${transaction.formattedDate}</div>
      // ...
   `;
   ```
5.  *Local Storage API*. Untuk menyimpan data pengguna secara lokal.
   ```sh
   localStorage.setItem('transactions', JSON.stringify(this.transactions));
   ```   
6. *Event Binding*. Menggunakan .bind(this) untuk mempertahankan konteks dalam event handlers.
   ```sh
   transactionForm.addEventListener('submit', this.handleNewTransaction.bind(this));
   ```
7. *Array Methods*. Menggunakan .filter(), .map(), dan .reduce() untuk manipulasi data.
   ```sh
   this.transactions = this.transactions.filter(t => t.id !== id);
   ```
8. *Async/Wait*. Untuk inisialisasi aplikasi secara asinkron.
   ```sh
   const initApp = async () => {
    try {
        const tracker = new FinancialTracker();
        // ...
    } catch (error) {
        console.error('Error initializing app:', error);
    }
   };
   ```
9. *Internationalization API*. Untuk format mata uang dan tanggal sesuai bahasa Indonesia.
    ```sh
    new Intl.NumberFormat('id-ID', { 
      style: 'currency', 
      currency: 'IDR',
      // ...
    }).format(amount);
    ``` 

## Struktur Proyek
```sh
// Project File Structures:
tugas/
│
├── index.html                # File HTML utama
├── css/                      # Folder untuk file CSS
│   └── style.css             # File CSS utama
└── js/                       # Folder untuk file JavaScript
    ├── app.js                # File JavaScript utama
    ├── Transaction.js        # Kelas Transaction
    └── FinancialTracker.js   # Kelas FinancialTracker
```
