# Multi-Agent System: Koordinasi Dua Robot pada Jalur Sempit

## 1. Deskripsi Proyek

Multi-Agent System (MAS) adalah sistem yang terdiri dari beberapa agen yang berinteraksi dalam suatu lingkungan untuk mencapai tujuan tertentu. Agen dapat bekerja sama, berkomunikasi, dan berkoordinasi untuk menyelesaikan masalah.

Menurut Wooldridge (2009), Multi-Agent System mempelajari sistem yang terdiri dari banyak agen yang berinteraksi. Agen dapat berupa program komputer atau robot yang bekerja secara mandiri.

Proyek ini merupakan simulasi sederhana Multi-Agent System menggunakan Python. Dua robot ingin melewati satu jalur sempit yang hanya dapat digunakan oleh satu robot pada satu waktu. Kedua robot harus berkoordinasi agar tidak menggunakan jalur secara bersamaan.

## 2. Studi Kasus

### Permasalahan

Terdapat dua robot, yaitu Robot A dan Robot B, yang ingin melewati jalur sempit untuk mencapai tujuan masing-masing.

Masalah yang dihadapi:
- Kedua robot membutuhkan jalur yang sama.
- Jalur hanya dapat digunakan oleh satu robot pada satu waktu.
- Tanpa koordinasi, kedua robot berpotensi berebut jalur.
- Sistem harus menentukan robot mana yang boleh melewati jalur terlebih dahulu.

### Solusi

Sistem menggunakan beberapa agen dengan peran berbeda. Setiap agen robot mengajukan permintaan penggunaan jalur, sedangkan agen pengatur jalur memberikan izin kepada satu robot pada satu waktu.

## 3. Agen yang Terlibat

| Agen | Peran |
|---|---|
| Robot A | Meminta akses jalur dan bergerak menuju tujuan |
| Robot B | Meminta akses jalur dan bergerak menuju tujuan |
| Corridor Coordinator | Mengatur akses jalur agar tidak digunakan dua robot secara bersamaan |

## 4. Arsitektur Sistem

```text
          Robot A
             |
             | Meminta akses
             v
    +---------------------+
    | Corridor Coordinator|
    +---------------------+
             ^
             | Meminta akses
             |
          Robot B
             |
             v
       Jalur Sempit
    (Satu robot pada satu waktu)
```

Coordinator bertindak sebagai agen koordinasi yang mengatur penggunaan sumber daya bersama, yaitu jalur sempit.

## 5. Alur Kerja Sistem

1. Robot A dan Robot B memiliki tujuan masing-masing.
2. Setiap robot mengajukan permintaan untuk menggunakan jalur.
3. Coordinator memeriksa apakah jalur sedang digunakan.
4. Jika jalur kosong, coordinator memberikan izin kepada satu robot.
5. Robot yang mendapat izin melewati jalur.
6. Setelah selesai, robot melepaskan akses jalur.
7. Robot berikutnya memperoleh kesempatan untuk melewati jalur.
8. Proses berulang sampai kedua robot mencapai tujuan.

## 6. Implementasi dengan Python

Program berikut merupakan simulasi berbasis aturan (rule-based), bukan model AI berbasis LLM atau machine learning.

```python
class CorridorCoordinator:
    def __init__(self):
        self.occupied = False

    def request_access(self, robot_name):
        if not self.occupied:
            self.occupied = True
            print(f"{robot_name} mendapat izin menggunakan jalur.")
            return True

        print(f"{robot_name} menunggu, jalur sedang digunakan.")
        return False

    def release_access(self, robot_name):
        self.occupied = False
        print(f"{robot_name} selesai dan melepaskan jalur.")


class RobotAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.finished = False

    def move(self, coordinator):
        if self.finished:
            return

        print(f"\n{self.name} meminta akses jalur.")

        if coordinator.request_access(self.name):
            print(f"{self.name} bergerak menuju {self.goal}.")
            self.finished = True
            coordinator.release_access(self.name)


def main():
    coordinator = CorridorCoordinator()

    robot_a = RobotAgent("Robot A", "Tujuan A")
    robot_b = RobotAgent("Robot B", "Tujuan B")

    # Simulasi ketika Robot A dan Robot B meminta jalur
    # pada waktu yang berdekatan.
    robot_a.move(coordinator)
    robot_b.move(coordinator)

    print("\nStatus akhir:")
    print(f"Robot A selesai: {robot_a.finished}")
    print(f"Robot B selesai: {robot_b.finished}")


if __name__ == "__main__":
    main()
```

## 7. Contoh Output

```text
Robot A meminta akses jalur.
Robot A mendapat izin menggunakan jalur.
Robot A bergerak menuju Tujuan A.
Robot A selesai dan melepaskan jalur.

Robot B meminta akses jalur.
Robot B mendapat izin menggunakan jalur.
Robot B bergerak menuju Tujuan B.
Robot B selesai dan melepaskan jalur.

Status akhir:
Robot A selesai: True
Robot B selesai: True
```

## 8. Analisis Hasil

Berdasarkan simulasi, coordinator mengatur penggunaan jalur sehingga hanya satu robot yang memperoleh akses pada satu waktu. Setelah Robot A selesai, Robot B dapat menggunakan jalur yang sama.

Sistem ini menunjukkan tiga konsep penting dalam Multi-Agent System:

- **Autonomy:** setiap robot memiliki tujuan dan perilaku sendiri.
- **Communication:** robot mengirimkan permintaan akses kepada coordinator.
- **Coordination:** coordinator mengatur akses terhadap sumber daya bersama.

Perlu diperhatikan bahwa simulasi ini memproses permintaan Robot A terlebih dahulu, kemudian Robot B. Program belum mensimulasikan pergerakan fisik, tabrakan nyata, atau permintaan yang berlangsung secara paralel.

## 9. Kelebihan dan Kekurangan

### Kelebihan
- Struktur program sederhana dan mudah dipahami.
- Setiap agen memiliki tanggung jawab yang jelas.
- Penggunaan jalur bersama dapat diatur melalui koordinasi.
- Dapat dikembangkan untuk simulasi robot yang lebih kompleks.

### Kekurangan
- Belum menggunakan sensor atau simulasi lingkungan fisik.
- Belum menggunakan komunikasi jaringan antarrobot.
- Belum menangani kegagalan robot atau coordinator.
- Belum menerapkan penjadwalan yang adil berdasarkan waktu tunggu.

## 10. Kesimpulan

Multi-Agent System dapat digunakan untuk menyelesaikan masalah koordinasi ketika beberapa agen memiliki tujuan masing-masing tetapi harus menggunakan sumber daya yang sama.

Dalam studi kasus ini, dua robot berbagi satu jalur sempit. Coordinator mengatur pemberian akses agar jalur tidak digunakan oleh dua robot secara bersamaan. Simulasi ini merupakan contoh dasar penerapan koordinasi antaragen dalam sistem robotika.

## 11. Referensi

1. Wooldridge, M. (2009). *An Introduction to MultiAgent Systems* (2nd ed.). Wiley.  
   https://www.wiley.com/en-us/An+Introduction+to+MultiAgent+Systems-p-978-0-470-51946-2

2. Wooldridge, M., & Jennings, N. R. (1995). Intelligent agents: Theory and practice. *The Knowledge Engineering Review, 10*(2), 115–152.  
   https://doi.org/10.1017/S0269888900008122

3. Microsoft. (n.d.). *Multi-agent Conversation Framework — AutoGen Documentation*.  
   https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat/

4. Microsoft. (n.d.). *Microsoft Agent Framework Documentation*.  
   https://learn.microsoft.com/en-us/agent-framework/

---

**Catatan:** kode di atas adalah implementasi demonstrasi yang dibuat untuk laporan ini, bukan kode yang diambil dari repository Orchestrator. Referensi digunakan untuk mendukung konsep MAS dan pengembangan sistem berbasis agen.
