# Artificial Intelligence (AI): Search System, Expert System, and Multiagent System

## Deskripsi

Repository ini berisi pembelajaran mengenai tiga konsep penting dalam Artificial Intelligence (AI), yaitu Search System, Expert System, dan Multiagent System. Setiap topik dilengkapi dengan definisi, fungsi dan kegunaan, contoh penerapan dalam kehidupan sehari-hari, serta implementasi program sederhana menggunakan bahasa pemrograman C.

---

# 1. Search System

## 1.1 Definisi

Search System atau sistem pencarian merupakan metode dalam Artificial Intelligence yang digunakan untuk menemukan solusi dari suatu permasalahan dengan menelusuri berbagai kemungkinan keadaan atau jalur.

Proses pencarian dimulai dari kondisi awal (*initial state*) menuju kondisi tujuan (*goal state*) melalui serangkaian langkah tertentu. Algoritma pencarian dapat menggunakan pendekatan seperti Breadth-First Search (BFS), Depth-First Search (DFS), dan A*.

## 1.2 Fungsi dan Kegunaan

Search System memiliki beberapa fungsi, yaitu:

- Menemukan jalur dari titik awal menuju titik tujuan.
- Menentukan solusi dari sekumpulan kemungkinan yang tersedia.
- Membantu pengambilan keputusan berdasarkan hasil pencarian.
- Mengoptimalkan pencarian solusi sesuai kriteria algoritma yang digunakan.

Contoh kegunaannya adalah pencarian rute pada aplikasi navigasi, pencarian data, pemecahan puzzle, dan perencanaan pergerakan robot otonom.

## 1.3 Contoh Penggunaan

Salah satu penerapan Search System adalah pada robot bergerak otonom (*Autonomous Mobile Robot* atau AMR) di lingkungan greenhouse.

Robot harus mencari jalur dari posisi awal menuju lokasi tanaman yang ingin diperiksa. Sistem merepresentasikan lingkungan sebagai kumpulan titik yang saling terhubung, kemudian menggunakan algoritma pencarian untuk menemukan jalur menuju tujuan.

Contoh lainnya:
- Google Maps dalam pencarian rute.
- Algoritma pencarian pada permainan catur.
- Robot yang mencari jalur menuju lokasi tertentu.
- Pencarian dokumen atau data dalam suatu sistem.

## 1.4 Contoh Program Sederhana (C)

Program berikut menerapkan algoritma Breadth-First Search (BFS) untuk menemukan jalur dari titik A menuju titik D pada sebuah graf.

**File: `search_system.c`**

```c
#include <stdio.h>

#define N 5

int main() {
    int graph[N][N] = {0};
    int visited[N] = {0};
    int parent[N];
    int queue[N];
    int front = 0, rear = 0;

    // Membuat hubungan antar titik
    graph[0][1] = graph[1][0] = 1; // A-B
    graph[0][2] = graph[2][0] = 1; // A-C
    graph[1][3] = graph[3][1] = 1; // B-D
    graph[2][4] = graph[4][2] = 1; // C-E
    graph[4][3] = graph[3][4] = 1; // E-D

    char node[N] = {'A', 'B', 'C', 'D', 'E'};

    int start = 0; // A
    int goal = 3;  // D

    for (int i = 0; i < N; i++)
        parent[i] = -1;

    queue[rear++] = start;
    visited[start] = 1;

    while (front < rear) {
        int current = queue[front++];

        if (current == goal)
            break;

        for (int i = 0; i < N; i++) {
            if (graph[current][i] && !visited[i]) {
                visited[i] = 1;
                parent[i] = current;
                queue[rear++] = i;
            }
        }
    }

    if (!visited[goal]) {
        printf("Jalur tidak ditemukan.\n");
    } else {
        int path[N], count = 0;

        for (int v = goal; v != -1; v = parent[v])
            path[count++] = v;

        printf("Jalur dari A ke D: ");

        for (int i = count - 1; i >= 0; i--) {
            printf("%c", node[path[i]]);

            if (i > 0)
                printf(" -> ");
        }

        printf("\n");
    }

    return 0;
}
```

**Contoh output:**

```text
Jalur dari A ke D: A -> B -> D
```

**Penjelasan:**

Program menggunakan BFS untuk menelusuri titik berdasarkan urutan tingkat kedekatan dari titik awal. Variabel `queue` menyimpan titik yang akan diperiksa, sedangkan `visited` mencegah titik dikunjungi berulang kali. Variabel `parent` digunakan untuk menyusun kembali jalur yang ditemukan.

Pada graf tanpa bobot, BFS dapat menemukan jalur dengan jumlah sisi paling sedikit.

---

# 2. Expert System

## 2.1 Definisi

Expert System atau sistem pakar adalah sistem berbasis Artificial Intelligence yang dirancang untuk meniru proses pengambilan keputusan seorang pakar pada bidang tertentu berdasarkan pengetahuan dan aturan yang telah ditentukan.

Sistem ini menggunakan basis pengetahuan (*knowledge base*) dan mekanisme penalaran (*inference engine*) untuk menghasilkan kesimpulan berdasarkan informasi yang diberikan pengguna.

## 2.2 Fungsi dan Kegunaan

Expert System memiliki beberapa fungsi, yaitu:

- Membantu pengguna menganalisis suatu permasalahan.
- Memberikan rekomendasi berdasarkan aturan yang tersedia.
- Menyimpan pengetahuan pakar agar dapat digunakan kembali.
- Mendukung pengambilan keputusan secara konsisten.
- Membantu pengguna memperoleh diagnosis atau solusi awal.

Expert System tidak selalu menggantikan pakar manusia. Sistem ini memiliki keterbatasan sesuai pengetahuan dan aturan yang dimasukkan ke dalamnya.

## 2.3 Contoh Penggunaan

Salah satu penerapan Expert System adalah diagnosis awal kerusakan komputer.

Pengguna memasukkan gejala yang dialami, seperti komputer tidak menyala atau komputer menyala tetapi layar gelap. Sistem kemudian mencocokkan gejala tersebut dengan aturan yang tersedia untuk memberikan kemungkinan penyebab dan saran pemeriksaan.

Contoh lainnya:
- Sistem diagnosis awal kerusakan kendaraan.
- Sistem pendukung diagnosis penyakit.
- Sistem rekomendasi pemeliharaan mesin.
- Sistem identifikasi penyakit tanaman.
- Sistem konsultasi berbasis aturan.

## 2.4 Contoh Program Sederhana (C)

Program berikut menggunakan aturan IF–THEN untuk menentukan kemungkinan masalah pada komputer.

**File: `expert_system.c`**

```c
#include <stdio.h>

int main() {
    int tidak_menyala;
    int lampu_mati;
    int layar_gelap;
    int komputer_lambat;

    printf("=== SISTEM PAKAR KOMPUTER ===\n");
    printf("Masukkan 1 untuk Ya dan 0 untuk Tidak.\n\n");

    printf("Komputer tidak menyala? ");
    scanf("%d", &tidak_menyala);

    printf("Lampu indikator mati? ");
    scanf("%d", &lampu_mati);

    printf("Komputer menyala tetapi layar gelap? ");
    scanf("%d", &layar_gelap);

    printf("Komputer terasa lambat? ");
    scanf("%d", &komputer_lambat);

    printf("\n=== HASIL DIAGNOSIS ===\n");

    if (tidak_menyala == 1 && lampu_mati == 1) {
        printf("Kemungkinan masalah: Sumber daya listrik.\n");
        printf("Saran: Periksa kabel daya dan power supply.\n");
    }
    else if (layar_gelap == 1) {
        printf("Kemungkinan masalah: Monitor atau koneksi display.\n");
        printf("Saran: Periksa kabel monitor.\n");
    }
    else if (komputer_lambat == 1) {
        printf("Kemungkinan masalah: Performa komputer menurun.\n");
        printf("Saran: Periksa penggunaan RAM, CPU, dan penyimpanan.\n");
    }
    else {
        printf("Diagnosis belum dapat ditentukan.\n");
        printf("Diperlukan pemeriksaan lebih lanjut.\n");
    }

    return 0;
}
```

**Contoh output:**

```text
=== SISTEM PAKAR KOMPUTER ===
Masukkan 1 untuk Ya dan 0 untuk Tidak.

Komputer tidak menyala? 1
Lampu indikator mati? 1
Komputer menyala tetapi layar gelap? 0
Komputer terasa lambat? 0

=== HASIL DIAGNOSIS ===
Kemungkinan masalah: Sumber daya listrik.
Saran: Periksa kabel daya dan power supply.
```

**Penjelasan:**

Program menerapkan aturan IF–THEN melalui kondisi `if`, `else if`, dan `else`. Ketika gejala yang dimasukkan memenuhi aturan tertentu, program menampilkan kesimpulan yang sesuai.

Pada contoh ini, aturan pengetahuan ditulis langsung di dalam kode. Untuk sistem pakar yang lebih kompleks, basis pengetahuan dapat dipisahkan dari program utama dan menggunakan metode penalaran seperti *forward chaining* atau *backward chaining*.

Hasil program merupakan perkiraan awal dan tidak menjamin penyebab kerusakan yang sebenarnya.

---

# 3. Multiagent System

## 3.1 Definisi

Multiagent System (MAS) adalah sistem dalam Artificial Intelligence yang terdiri dari dua atau lebih agen (*agent*) yang bekerja dalam suatu lingkungan untuk mencapai tujuan tertentu.

Setiap agen dapat memiliki tugas, kemampuan, informasi, dan tujuan masing-masing. Agen dapat bekerja secara mandiri maupun berinteraksi, berkomunikasi, dan berkoordinasi dengan agen lainnya.

Multiagent System digunakan ketika suatu permasalahan lebih mudah ditangani dengan membagi pekerjaan kepada beberapa agen dibandingkan mengandalkan satu agen saja.

## 3.2 Fungsi dan Kegunaan

Multiagent System memiliki beberapa fungsi, yaitu:

- Membagi pekerjaan menjadi beberapa tugas yang dapat ditangani oleh agen berbeda.
- Memungkinkan beberapa agen bekerja secara bersamaan.
- Mendukung koordinasi dan pertukaran informasi.
- Membantu menyelesaikan permasalahan yang kompleks.
- Meningkatkan fleksibilitas sistem melalui pembagian tanggung jawab.

Keberhasilan sistem bergantung pada cara agen berkoordinasi. Banyaknya agen tidak selalu membuat sistem lebih efisien apabila terjadi konflik atau komunikasi yang buruk.

## 3.3 Contoh Penggunaan

Contoh penerapan Multiagent System adalah sistem pemantauan dan pengendalian lingkungan greenhouse.

Dalam sistem ini, terdapat dua agen dengan tugas berbeda:

1. **Monitoring Agent:** Memantau suhu lingkungan greenhouse.
2. **Control Agent:** Menentukan apakah kipas perlu dinyalakan berdasarkan informasi suhu.

Monitoring Agent memberikan informasi kepada Control Agent. Selanjutnya, Control Agent menentukan tindakan berdasarkan aturan yang telah ditentukan.

Contoh lainnya:
- Sekumpulan robot yang bekerja sama di gudang.
- Sistem lampu lalu lintas yang berkoordinasi.
- Simulasi kendaraan otonom.
- Sistem perdagangan otomatis dengan beberapa agen.
- Pengelolaan energi pada bangunan pintar.

## 3.4 Contoh Program Sederhana (C)

Program berikut mensimulasikan dua agen pada greenhouse. Agen pertama membaca suhu, sedangkan agen kedua menentukan tindakan pengendalian kipas.

**File: `multiagent_system.c`**

```c
#include <stdio.h>

// Agent 1: Monitoring suhu
int monitoring_agent() {
    int suhu;

    printf("Masukkan suhu greenhouse (C): ");
    scanf("%d", &suhu);

    printf("Monitoring Agent: Suhu terdeteksi %d C.\n", suhu);

    return suhu;
}

// Agent 2: Pengendali kipas
void control_agent(int suhu) {
    printf("Control Agent: ");

    if (suhu >= 30) {
        printf("Kipas dinyalakan.\n");
    }
    else {
        printf("Kipas tidak perlu dinyalakan.\n");
    }
}

int main() {
    int suhu;

    printf("=== MULTIAGENT SYSTEM GREENHOUSE ===\n");

    suhu = monitoring_agent();

    control_agent(suhu);

    return 0;
}
```

**Contoh output:**

```text
=== MULTIAGENT SYSTEM GREENHOUSE ===
Masukkan suhu greenhouse (C): 32
Monitoring Agent: Suhu terdeteksi 32 C.
Control Agent: Kipas dinyalakan.
```

**Penjelasan:**

Program membagi tugas menjadi dua fungsi yang merepresentasikan dua agen:

- `monitoring_agent()` menerima dan melaporkan data suhu.
- `control_agent()` menerima data suhu dan menentukan tindakan berdasarkan aturan.

Kedua agen mempunyai tanggung jawab berbeda dan saling terhubung melalui informasi suhu. Contoh ini merupakan simulasi konseptual sederhana; program belum mengimplementasikan komunikasi agen yang kompleks, proses paralel, atau protokol koordinasi.

Dalam implementasi nyata, Monitoring Agent dapat memperoleh data dari sensor suhu, sedangkan Control Agent dapat mengirimkan perintah ke perangkat pengendali kipas.

---

# 4. Cara Menjalankan Program

Ketiga program menggunakan bahasa C dan dapat dijalankan menggunakan compiler GCC.

## 4.1 Persiapan

Pastikan GCC telah terpasang. Periksa instalasi melalui terminal:

```bash
gcc --version
```

## 4.2 Kompilasi dan eksekusi

**Search System**

```bash
gcc search_system.c -o search_system
```

Windows:

```bash
search_system.exe
```

Linux:

```bash
./search_system
```

**Expert System**

```bash
gcc expert_system.c -o expert_system
```

Windows:

```bash
expert_system.exe
```

Linux:

```bash
./expert_system
```

**Multiagent System**

```bash
gcc multiagent_system.c -o multiagent_system
```

Windows:

```bash
multiagent_system.exe
```

Linux:

```bash
./multiagent_system
```

## 4.3 Struktur Repository

Susunan file yang disarankan:

```text
artificial-intelligence/
├── README.md
├── search_system.c
├── expert_system.c
└── multiagent_system.c
```

Setiap file program memiliki fungsi yang berbeda sehingga dapat dipelajari dan dijalankan secara terpisah.

---

# 5. Kesimpulan

Search System, Expert System, dan Multiagent System merupakan tiga konsep yang memiliki pendekatan berbeda dalam Artificial Intelligence.

- **Search System** berfokus pada pencarian jalur atau solusi melalui penelusuran berbagai kemungkinan.
- **Expert System** berfokus pada pengambilan kesimpulan berdasarkan pengetahuan dan aturan yang telah ditentukan.
- **Multiagent System** berfokus pada interaksi dan koordinasi beberapa agen untuk menyelesaikan suatu permasalahan.

Ketiganya dapat diterapkan dalam berbagai bidang, termasuk robotika, sistem kendali, diagnosis, dan otomasi. Melalui implementasi sederhana menggunakan bahasa C, konsep dasar masing-masing sistem dapat dipahami sebelum dikembangkan menjadi aplikasi AI yang lebih kompleks.

## Referensi

- Russell, S. J., & Norvig, P. *Artificial Intelligence: A Modern Approach*. Pearson.
- [GitHub — Search Algorithm](https://github.com/topics/search-algorithm)
- [GitHub — Expert System](https://github.com/topics/expert-system)
- [GitHub — Multiagent Systems](https://github.com/topics/multiagent-system)
- [GCC — GNU Compiler Collection](https://gcc.gnu.org/)

---

Kelompok 2:
Manager: Nabilla Rachmadhani (101022300161)
Developer 1: Wahyu Aksania Tazzaka Wijanarko (101022330025)
Developer 2: Indah Natalia Nadeak (101022300167)