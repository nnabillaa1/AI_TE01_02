# Expert System: Sistem Pakar Diagnosis Kerusakan Komputer

## 1. Deskripsi Proyek

Expert System atau Sistem Pakar merupakan salah satu penerapan Artificial Intelligence (AI) yang dirancang untuk meniru cara seorang pakar mengambil keputusan berdasarkan pengetahuan dan aturan tertentu.

Proyek ini bertujuan untuk membuat sistem pakar sederhana menggunakan bahasa pemrograman Python untuk membantu pengguna mengidentifikasi kemungkinan kerusakan komputer berdasarkan gejala yang dialami.

Sistem menggunakan pendekatan **Rule-Based System** dengan aturan IF–THEN untuk mencocokkan gejala dengan kemungkinan penyebab kerusakan.

## 2. Tujuan

- Memahami konsep dasar Expert System dalam AI.
- Mempelajari penggunaan knowledge base dan aturan IF–THEN.
- Mengimplementasikan sistem pakar sederhana menggunakan Python.
- Menghasilkan diagnosis awal berdasarkan gejala yang dipilih pengguna.

## 3. Konsep Sistem Pakar

Sistem pakar terdiri dari beberapa komponen utama:

| Komponen | Fungsi |
|---|---|
| Knowledge Base | Menyimpan pengetahuan dan aturan tentang kerusakan komputer. |
| Inference Engine | Mencocokkan gejala dengan aturan yang tersedia. |
| User Interface | Menjadi media interaksi antara pengguna dan program. |
| Working Memory | Menyimpan gejala yang dimasukkan selama proses diagnosis. |

## 4. Metode yang Digunakan

Metode yang digunakan adalah **Rule-Based Reasoning**, yaitu pengambilan keputusan berdasarkan aturan yang telah ditentukan.

Contoh aturan:

- IF komputer tidak menyala AND lampu indikator mati, THEN kemungkinan masalah pada sumber daya listrik.
- IF komputer menyala AND layar tidak menampilkan gambar, THEN kemungkinan masalah pada monitor atau koneksi display.
- IF komputer terasa lambat AND banyak aplikasi berjalan, THEN kemungkinan penggunaan sumber daya terlalu tinggi.

Aturan tersebut merupakan contoh sederhana untuk pembelajaran, bukan hasil diagnosis teknis yang pasti.

## 5. Struktur Repository

```text
expert-system/
├── README.md
├── main.py
└── requirements.txt
```

Keterangan:
- `README.md`: Dokumentasi proyek.
- `main.py`: Program utama sistem pakar.
- `requirements.txt`: Daftar library yang diperlukan.

## 6. Cara Menjalankan Program

1. Pastikan Python sudah terpasang.
2. Clone repository:

   ```bash
   git clone https://github.com/USERNAME/expert-system.git
   ```

3. Masuk ke folder proyek:

   ```bash
   cd expert-system
   ```

4. Jalankan program:

   ```bash
   python main.py
   ```

Program ini menggunakan library bawaan Python sehingga tidak memerlukan instalasi library tambahan.

## 7. Contoh Input dan Output

**Input:**
- Komputer tidak menyala.
- Lampu indikator tidak menyala.

**Output:**
```text
=== HASIL DIAGNOSIS ===
Kemungkinan masalah: Sumber daya listrik.
Saran: Periksa kabel daya, stopkontak, dan power supply.
```

Hasil diagnosis merupakan perkiraan berdasarkan aturan yang tersedia.

## 8. Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:
- Menambahkan lebih banyak aturan diagnosis.
- Membuat antarmuka menggunakan Tkinter atau Streamlit.
- Menambahkan tingkat keyakinan pada hasil diagnosis.
- Mengembangkan knowledge base berdasarkan dokumentasi teknis yang tepercaya.

## 9. Referensi GitHub

1. Experta – Library Python untuk membangun sistem pakar berbasis aturan: https://github.com/nilp0inter/experta
2. PyKnow – Implementasi sistem pakar berbasis Python: https://github.com/buguroo/pyknow
3. GitHub Topics: Expert System – Kumpulan repository terkait sistem pakar: https://github.com/topics/expert-system

## 10. Kesimpulan

Expert System dapat membantu proses pengambilan keputusan dengan memanfaatkan pengetahuan dan aturan yang telah didefinisikan. Melalui proyek ini, konsep dasar AI dapat dipelajari dengan membuat program yang menghubungkan gejala, aturan, dan hasil diagnosis.

## 11. Contoh Program Python

```

def diagnosis_komputer():
    print("=== SISTEM PAKAR DIAGNOSIS KOMPUTER ===")
    print("Jawab pertanyaan dengan y (ya) atau t (tidak).\n")

    tidak_menyala = input("Apakah komputer tidak menyala? (y/t): ").lower()
    lampu_mati = input("Apakah lampu indikator mati? (y/t): ").lower()

    layar_gelap = input("Apakah komputer menyala tetapi layar gelap? (y/t): ").lower()
    komputer_lambat = input("Apakah komputer terasa lambat? (y/t): ").lower()
    banyak_aplikasi = input("Apakah banyak aplikasi berjalan? (y/t): ").lower()

    print("\n=== HASIL DIAGNOSIS ===")

    if tidak_menyala == "y" and lampu_mati == "y":
        print("Kemungkinan masalah: Sumber daya listrik.")
        print("Saran: Periksa kabel daya, stopkontak, dan power supply.")

    elif layar_gelap == "y":
        print("Kemungkinan masalah: Monitor atau koneksi display.")
        print("Saran: Periksa kabel monitor dan koneksi display.")

    elif komputer_lambat == "y" and banyak_aplikasi == "y":
        print("Kemungkinan masalah: Penggunaan sumber daya terlalu tinggi.")
        print("Saran: Tutup aplikasi yang tidak digunakan.")

    elif komputer_lambat == "y":
        print("Kemungkinan masalah: Performa komputer menurun.")
        print("Saran: Periksa penggunaan RAM, CPU, dan penyimpanan.")

    else:
        print("Diagnosis belum dapat ditentukan.")
        print("Diperlukan pemeriksaan gejala lebih lanjut.")

    print("\nCatatan: Hasil ini merupakan diagnosis awal.")


if __name__ == "__main__":
    diagnosis_komputer()

```
---

**Technology:** Python  
**Category:** Artificial Intelligence (AI)  
**Project Type:** Rule-Based Expert System
