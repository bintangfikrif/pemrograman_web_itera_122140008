# Aplikasi Manajemen Buku Pribadi

Aplikasi Manajemen Buku Pribadi adalah aplikasi web berbasis React yang memungkinkan pengguna untuk mencatat, mengelola, dan melacak koleksi buku yang dimiliki, sedang dibaca, atau ingin dibeli. Aplikasi ini dirancang dengan user interface yang sederhana dan intuitif, serta memanfaatkan berbagai fitur modern dari React.

## Link Website
https://aplikasi-manajemen-buku.vercel.app/

## Fitur

Aplikasi ini menyediakan beberapa fitur utama:

### Manajemen Buku

- Menambahkan buku baru dengan judul, penulis, dan status (dimiliki, sedang dibaca, ingin dibeli)
- Mengedit informasi buku yang sudah ada
- Menghapus buku dari koleksi

### Pencarian dan Filter

- Mencari buku berdasarkan judul atau penulis
- Memfilter buku berdasarkan status

### Statistik Koleksi

- Melihat ringkasan koleksi buku (total buku, jumlah per status)
- Daftar buku terbaru yang ditambahkan

### Penyimpanan Lokal

- Semua data buku disimpan di localStorage browser

## Screenshoot Aplikasi

1. Tampilan Home
   ![image](https://github.com/user-attachments/assets/bbf1e866-f57c-4623-a432-867c8149b6bc)

2. Tampilan Statistik
   ![image](https://github.com/user-attachments/assets/914d6d55-656d-43c9-aa09-e036e1b8d305)

3. Tampilan Form Menambah Koleksi Buku
   ![image](https://github.com/user-attachments/assets/99b9e648-332d-4091-993e-b29744453f19)

4. Tampilan Koleksi Buku
   ![image](https://github.com/user-attachments/assets/6ee96075-5f13-4392-8d84-98b9c35aa189)

5. Tampilan Statistik Buku Setelah Ditambahkan
    ![image](https://github.com/user-attachments/assets/d71f0ceb-480f-4f41-9e3d-ba68b9bde7bc)
   
## Teknologi

Aplikasi ini dibangun menggunakan:
- React - Library JavaScript untuk membangun user interface
- React Router - Untuk navigasi antar halaman
- localStorage API - Untuk menyimpan data di browser
- Context API - Untuk manajemen state global
- CSS - Untuk styling komponen

## Instalasi

Untuk menginstal dan menjalankan aplikasi ini di komputer lokal, ikuti langkah-langkah berikut:

1. Clone repository
```
git clone [URL_REPOSITORY]
cd aplikasi-manajemen-buku
```
2. Instalasi dependensi
```
npm install
```
3. Jalankan Aplikasi
```
npm start
```
4. Akses aplikasi
Buka browser dan akses http://localhost:3000

## Penggunaan

### Halaman Utama:

- Untuk menambahkan buku, klik tombol "Tambah Buku" dan isi formulir yang muncul
- Untuk mengedit atau menghapus buku, gunakan tombol yang tersedia pada kartu buku
- Untuk mencari buku, gunakan kotak pencarian di bagian atas
- Untuk memfilter buku berdasarkan status, gunakan dropdown filter di bagian atas

### Halaman Statistik:

- Akses halaman ini dengan mengklik tab "Statistik" di menu navigasi
- Lihat ringkasan jumlah buku berdasarkan status
- Lihat daftar buku terbaru yang ditambahkan

## Struktur Folder

src/
├── components/
│   ├── BookForm/
│   │   ├── BookForm.js
│   │   └── BookForm.css
│   ├── BookList/
│   │   ├── BookList.js
│   │   └── BookList.css
│   └── BookFilter/
│       ├── BookFilter.js
│       └── BookFilter.css
├── pages/
│   ├── Home/
│   │   ├── Home.js
│   │   └── Home.css
│   └── Stats/
│       ├── Stats.js
│       └── Stats.css
├── hooks/
│   ├── useLocalStorage.js
│   └── useBookStats.js
├── context/
│   └── BookContext.js
└── App.js

## Penjelasan Implementasi 

Aplikasi ini mengimplementasikan beberapa konsep dan fitur penting dari React:

1. **Functional Components & Hooks**
Semua komponen diimplementasikan sebagai functional components dengan memanfaatkan berbagai React Hooks:

-**useState:** Untuk mengelola state lokal di dalam komponen
```
const [showAddForm, setShowAddForm] = useState(false);
```
-**useEffect**: Untuk menjalankan side-effects, seperti memfilter buku saat kriteria pencarian berubah
```
useEffect(() => {
  // Filter books based on search term and status
  // ...
}, [books, filter, searchTerm]);
```
-**useContext**: Untuk mengakses state global dari React Context
```
const { books, deleteBook } = useContext(BookContext);
```

2. **Custom Hooks**
Aplikasi mengimplementasikan dua custom hooks:
- **useLocalStorage**: Untuk menyimpan dan mengelola data di localStorage
```
function useLocalStorage(key, initialValue) {
  // Implementation for localStorage management
  // ...
  return [storedValue, setValue];
}
```
- **useBookStats**: Untuk menghitung statistik buku secara efisien dengan useMemo
```
function useBookStats() {
  const { books } = useContext(BookContext);
  const stats = useMemo(() => {
    // Calculate statistics
    // ...
    return { total, owned, reading, wishlist, recentBooks };
  }, [books]);
  return stats;
}
```

3. **Context API**
Context API digunakan untuk manajemen state global, memungkinkan semua komponen mengakses dan memodifikasi daftar buku tanpa prop drilling:
```
const BookContext = createContext();

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books', []);
  // Other state and functions
  // ...
  
  return (
    <BookContext.Provider value={{ books, addBook, editBook, deleteBook, /* ... */ }}>
      {children}
    </BookContext.Provider>
  );
}
```
4. **React Router**
React Router digunakan untuk implementasi navigasi multi-halaman tanpa reload halaman:
```
<Router>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/stats" element={<Stats />} />
  </Routes>
</Router>
```
5. **PropTypes**
PropTypes digunakan untuk validasi tipe props untuk memastikan keamanan tipe data:
```
BookForm.propTypes = {
  bookToEdit: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.string,
    notes: PropTypes.string
  }),
  onCancel: PropTypes.func
};
```
6. **Error Handling**
Aplikasi menerapkan penanganan kesalahan untuk validasi input form:
```
const validateForm = () => {
  const newErrors = {};
  if (!formData.title.trim()) newErrors.title = 'Judul buku wajib diisi';
  if (!formData.author.trim()) newErrors.author = 'Penulis buku wajib diisi';
  
  setErrors(newErrors);
  return Object.keys(newErrors).length === 0;
};
``` 
