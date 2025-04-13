# 📚 Personal To-Do Dashboard untuk Gweh

Aplikasi **Personal Dashboard** ini dirancang khusus untuk kebutuhan mahasiswa dan saya sendiri dalam mengelola daftar tugas. Kamu dapat menambahkan, mengedit, menandai selesai, serta menghapus tugas secara interaktif. Tugas disimpan secara lokal menggunakan `localStorage`, sehingga data tetap aman meskipun halaman di-refresh.

---

## ✨ Fitur Utama

- ✅ Tambah tugas dengan **judul** dan **tanggal deadline**
- ✏️ Edit tugas langsung dari tampilan
- ✅ Tandai tugas selesai atau pilih semua dan klik selesai, **terhapus setelah 3 detik**
- 🔔 Menampilkan notifikasi "Alhamdulillah, tugas selesai!"
- 📅 **Urutkan tugas berdasarkan deadline** secara otomatis
- 💾 Menyimpan data di `localStorage`
- 🎨 UI modern, minimalis, dan enak dilihat dengan aksen biru

---

## 🚀 Fitur ES6+ yang Diimplementasikan

| Fitur ES6+             | Implementasi                                                                  |
| ---------------------- | ----------------------------------------------------------------------------- |
| `let` & `const`        | Untuk deklarasi variabel agar lebih aman dan readable                         |
| Arrow Functions (`=>`) | `getTasks`, `saveTasks`, `renderTasks`, `addTask`, `editTask`, `completeTask` |
| Template Literals      | Contoh: `taskDiv.id = \`task-${task.id}\``                                    |
| Fungsi Asinkron        | `async/await` digunakan untuk delay render di awal                            |
| `class`                | Class `Task` digunakan untuk membuat objek tugas                              |

---

## 📷 Screenshot

![screenshot]([https://via.placeholder.com/800x400.png?text=Personal+To-Do+Dashboard](https://drive.google.com/file/d/1KJJSNM4wAQ5VNjzs3x-DpcaB3hfYHkVc/view?usp=sharing))

> Ganti link `placeholder` di atas dengan screenshot asli dari aplikasi kamu saat sudah dideploy atau dijalankan lokal.

---

## 📁 Cara Menjalankan

1. Cukup buka file HTML ini di browser (offline atau online).
2. Tidak perlu setup tambahan.
3. Semua data akan disimpan di browser (localStorage).
