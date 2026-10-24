# Search System dan Search Algorithm dalam Kecerdasan Buatan

## 1. Pendahuluan

Dalam bidang Kecerdasan Buatan (*Artificial Intelligence* atau AI), pencarian merupakan salah satu metode yang digunakan untuk menyelesaikan masalah dengan menemukan solusi berdasarkan kondisi awal, kemungkinan tindakan, dan tujuan yang ingin dicapai. Sistem pencarian (*Search System*) memungkinkan komputer mengeksplorasi berbagai kemungkinan untuk menemukan informasi, menentukan jalur, atau memperoleh solusi dari suatu permasalahan. Proses pencarian tersebut dilakukan menggunakan algoritma tertentu yang menentukan urutan eksplorasi dan cara memilih solusi. Salah satu penerapannya adalah pencarian jalur terpendek dalam peta atau labirin.

## 2. Definisi Search System

*Search System* adalah sistem yang digunakan untuk mencari informasi atau menemukan solusi dari suatu permasalahan berdasarkan kriteria dan tujuan tertentu. Dalam konteks kecerdasan buatan, sistem pencarian bekerja dengan mengeksplorasi *state space*, yaitu kumpulan keadaan atau kemungkinan yang dapat dicapai dari kondisi awal melalui serangkaian tindakan.

Sementara itu, *Search Algorithm* merupakan algoritma yang mengatur bagaimana proses pencarian dilakukan. Algoritma ini menentukan urutan pemeriksaan setiap keadaan, cara mengevaluasi kemungkinan solusi, dan kondisi ketika pencarian dihentikan.

Secara umum, komponen utama dalam proses pencarian meliputi:

- **Initial State:** kondisi atau posisi awal pencarian.
- **State Space:** kumpulan seluruh keadaan yang mungkin dijelajahi.
- **Actions:** tindakan yang dapat dilakukan untuk berpindah dari satu keadaan ke keadaan lainnya.
- **Goal State:** kondisi akhir yang ingin dicapai.
- **Search Strategy:** strategi yang menentukan urutan eksplorasi keadaan.
- **Solution Path:** urutan langkah yang menghubungkan kondisi awal dengan tujuan.

Menurut Russell dan Norvig dalam buku *Artificial Intelligence: A Modern Approach*, pencarian merupakan salah satu pendekatan penting dalam pemecahan masalah menggunakan kecerdasan buatan.

## 3. Kegunaan atau Fungsi Search System

Search System memiliki beberapa fungsi penting dalam pengembangan sistem kecerdasan buatan, antara lain:

1. **Menemukan solusi permasalahan.** Membantu sistem menemukan keadaan yang memenuhi tujuan tertentu dari berbagai kemungkinan yang tersedia.
2. **Menentukan jalur atau rute.** Digunakan untuk menemukan jalur dari lokasi awal menuju lokasi tujuan, seperti pada sistem navigasi dan robotika.
3. **Mengeksplorasi kemungkinan keputusan.** Membantu sistem mengevaluasi berbagai alternatif tindakan sebelum menentukan langkah berikutnya.
4. **Mengoptimalkan proses pencarian.** Algoritma tertentu dapat mencari solusi dengan jumlah langkah, biaya, atau waktu yang lebih efisien.
5. **Mendukung pengambilan keputusan otomatis.** Memungkinkan agen cerdas menentukan tindakan berdasarkan kondisi awal, tujuan, dan strategi pencarian yang digunakan.

Keberhasilan suatu algoritma pencarian dapat dievaluasi berdasarkan kelengkapan (*completeness*), optimalitas (*optimality*), kompleksitas waktu (*time complexity*), dan kompleksitas ruang (*space complexity*).

## 4. Jenis-Jenis Search Algorithm

Beberapa algoritma pencarian yang umum digunakan dalam kecerdasan buatan adalah sebagai berikut.

| Algoritma | Penjelasan |
|---|---|
| Breadth-First Search (BFS) | Menjelajahi simpul berdasarkan tingkat kedalaman, dimulai dari simpul yang paling dekat dengan kondisi awal. |
| Depth-First Search (DFS) | Menjelajahi satu cabang sedalam mungkin sebelum kembali ke cabang lainnya. |
| Uniform-Cost Search (UCS) | Memilih jalur dengan biaya kumulatif paling rendah. |
| Greedy Best-First Search | Memilih simpul berdasarkan perkiraan kedekatannya dengan tujuan menggunakan fungsi heuristik. |
| A* Search | Menggabungkan biaya yang telah ditempuh dan perkiraan biaya menuju tujuan untuk menentukan simpul yang dieksplorasi. |

Algoritma tersebut memiliki karakteristik dan kelebihan yang berbeda. Pemilihannya bergantung pada struktur permasalahan, ketersediaan informasi, biaya pencarian, dan kebutuhan untuk memperoleh solusi optimal.

## 5. Contoh Penggunaan Search System

Search System dapat diterapkan dalam berbagai bidang, antara lain:

1. **Navigasi dan pencarian rute:** algoritma A* dapat digunakan untuk mencari rute dari lokasi awal menuju lokasi tujuan berdasarkan jarak yang telah ditempuh dan estimasi jarak yang tersisa.
2. **Penyelesaian labirin:** BFS atau DFS dapat digunakan untuk menjelajahi jalur yang tersedia hingga menemukan pintu keluar.
3. **Robotika:** algoritma pencarian dapat membantu robot menentukan jalur pergerakan dari satu titik menuju titik lainnya.
4. **Permainan berbasis komputer:** algoritma pencarian digunakan untuk mengevaluasi kemungkinan langkah dalam permainan, misalnya dengan Minimax.
5. **Pencarian informasi:** sistem pencarian dapat menemukan dokumen atau informasi berdasarkan kata kunci dan kriteria tertentu.

Contoh sederhana dalam tugas ini adalah pencarian jalur pada sebuah graf menggunakan algoritma Breadth-First Search (BFS).

## 6. Contoh Program Sederhana: Breadth-First Search (BFS)

### 6.1 Deskripsi Program

Breadth-First Search (BFS) adalah algoritma pencarian yang menjelajahi simpul berdasarkan tingkat kedalaman. BFS memeriksa seluruh tetangga dari suatu simpul sebelum melanjutkan ke simpul pada tingkat berikutnya.

Algoritma ini menggunakan struktur data *queue* dengan prinsip *First In, First Out* (FIFO). Untuk graf yang tidak berbobot, BFS dapat menemukan jalur dengan jumlah sisi paling sedikit, selama seluruh simpul dan sisi yang relevan dapat dijelajahi.

### 6.2 Kode Program Python

Program berikut menggunakan graf sederhana yang menggambarkan hubungan antarposisi. Tujuannya adalah mencari jalur dari simpul `A` menuju simpul `G`.

```python
from collections import deque

# Representasi graf
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        # Periksa apakah tujuan telah ditemukan
        if current == goal:
            return path

        # Jelajahi tetangga simpul saat ini
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

# Menjalankan pencarian
start_node = 'A'
goal_node = 'G'

result = bfs(graph, start_node, goal_node)

if result:
    print("Jalur ditemukan:", " -> ".join(result))
else:
    print("Jalur tidak ditemukan.")
```

### 6.3 Hasil Program

Output program:

```text
Jalur ditemukan: A -> B -> E -> G
```

### 6.4 Penjelasan Program

Program dimulai dari simpul `A`, kemudian memasukkan jalur awal ke dalam antrean (*queue*). Selanjutnya, BFS memeriksa simpul berdasarkan urutan masuk ke antrean dan menambahkan tetangga yang belum dikunjungi. Setiap kali simpul tujuan `G` ditemukan, program mengembalikan jalur yang menghubungkan simpul awal dengan tujuan.

Pada graf tersebut, terdapat dua kemungkinan jalur menuju `G`, yaitu `A -> B -> E -> G` dan `A -> C -> F -> G`. Karena kedua jalur memiliki jumlah sisi yang sama, BFS menemukan salah satu jalur terpendek berdasarkan urutan tetangga dalam representasi graf.

Penggunaan `deque` dari modul `collections` memungkinkan operasi antrean dilakukan secara efisien. Modul tersebut merupakan bagian dari pustaka standar Python sehingga tidak memerlukan instalasi paket tambahan.

## 7. Cara Menjalankan Program

Untuk menjalankan program, ikuti langkah-langkah berikut:

1. Pastikan Python telah terpasang pada komputer.
2. Buat file bernama `bfs_search.py`.
3. Salin kode program BFS ke dalam file tersebut.
4. Buka terminal atau Command Prompt pada direktori tempat file disimpan.
5. Jalankan perintah berikut:

   ```bash
   python bfs_search.py
   ```

6. Periksa hasil pencarian yang ditampilkan pada terminal.

Program juga dapat dijalankan melalui Google Colab atau lingkungan pengembangan Python lainnya.

## 8. Kesimpulan

Search System merupakan salah satu konsep fundamental dalam kecerdasan buatan yang memungkinkan komputer menemukan solusi melalui eksplorasi berbagai kemungkinan keadaan. Search Algorithm berperan dalam menentukan strategi dan urutan eksplorasi agar proses pencarian sesuai dengan tujuan yang ditetapkan. Setiap algoritma memiliki karakteristik yang berbeda sehingga pemilihannya harus disesuaikan dengan kebutuhan permasalahan. Melalui implementasi BFS menggunakan Python, konsep pencarian dapat dipahami secara praktis dengan mencari jalur dari simpul awal menuju simpul tujuan pada suatu graf.

## 9. Daftar Referensi

1. Russell, S. J., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. [https://aima.eecs.berkeley.edu/](https://aima.eecs.berkeley.edu/)

2. University of Edinburgh. (n.d.). *INF2D: Search Strategies*. [https://opencourse.inf.ed.ac.uk/inf2d/course-materials/week-1/lecture-3](https://opencourse.inf.ed.ac.uk/inf2d/course-materials/week-1/lecture-3)

3. Python Software Foundation. (n.d.). *collections — Container Datatypes*. Python Documentation. [https://docs.python.org/3/library/collections.html](https://docs.python.org/3/library/collections.html)

---

**Catatan:** Contoh program pada README ini menggunakan Breadth-First Search (BFS) sebagai implementasi dasar. Program dapat dikembangkan lebih lanjut dengan algoritma DFS, UCS, atau A* untuk membandingkan strategi pencarian dan karakteristik kinerjanya.