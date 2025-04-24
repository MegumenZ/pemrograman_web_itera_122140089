
# Aplikasi Manajemen Buku Pribadi

Aplikasi berbasis web untuk mencatat dan mengelola daftar buku pribadi, seperti buku yang dimiliki, sedang dibaca, atau ingin dibeli.

---

## Fitur Utama

- Tambah buku baru (judul, penulis, dan status: milik, sedang dibaca, atau ingin dibeli)
- Edit dan hapus data buku
- Filter buku berdasarkan status
- Pencarian buku berdasarkan judul
- Menyimpan data di `localStorage`
- Halaman statistik: total buku, per kategori, dan lainnya

---

## Teknologi yang Digunakan

- React
- Context API untuk manajemen state global
- React Router untuk navigasi antar halaman
- Custom Hooks: `useLocalStorage`, `useBookStats`
- React Testing Library untuk unit testing
- PropTypes untuk pengecekan tipe data props

---

## 🗂️ Struktur Proyek

```
src/
├── components/
│   ├── BookForm/
│   ├── BookList/
│   └── BookFilter/
├── pages/
│   ├── Home/
│   └── Stats/
├── hooks/
│   ├── useLocalStorage.js
│   └── useBookStats.js
├── context/
│   └── BookContext.js
├── App.jsx
└── main.jsx
```

---

## 📸 Screenshot Antarmuka

![Beranda Aplikasi](https://i.imgur.com/6oV6ZNA.png)
)
![Statistik Buku](https://i.imgur.com/b7qOKLb.png)
)

---

## ⚙️ Cara Menjalankan Aplikasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/MegumenZ/pemrograman_web_itera_122140089.git
   ```

2. Masuk ke folder proyek:
   ```bash
   cd pemrograman_web_itera_122140089
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Jalankan server pengembangan:
   ```bash
   npm run dev
   ```

5. Akses aplikasi di:
   ```
   http://localhost:5173
   ```

---

## ✅ Testing

Telah dibuat minimal **5 unit test** menggunakan **React Testing Library**:

```bash
npm run test
```

---

## Penanganan Error

- Form input akan memunculkan pesan error jika judul atau penulis kosong.
- Sistem validasi dilakukan sebelum data disimpan.

---

## Catatan

- Aplikasi menyimpan data buku ke **localStorage**, sehingga tidak hilang saat refresh.
- UI menggunakan **tema biru** dengan gaya bersih dan modern, terinspirasi dari desain situs Perpusnas.

