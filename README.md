#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TASKS 5

// Representasi struktur Map_Obj dalam bentuk struct C
typedef struct {
    int task_num;
    int start_pos;
    int goal_pos;
    char str_map[256]; // Representasi string map
} Map_Obj;

// Fungsi untuk inisialisasi Map (menggantikan Map_Obj(task_num))
Map_Obj create_map(int task_num) {
    Map_Obj task_map;
    task_map.task_num = task_num;
    task_map.start_pos = 0;   // Contoh nilai awal
    task_map.goal_pos = 10;   // Contoh nilai tujuan
    snprintf(task_map.str_map, sizeof(task_map.str_map), "Map for Task %d", task_num);
    return task_map;
}

// Simulasi algoritma A* (mengembalikan panjang path atau array path)
int* a_star(Map_Obj *map) {
    // Alokasi memori untuk path simulasi
    static int path[10];
    // Isi dengan logika A* Anda di sini
    return path;
}

// Menandai path pada map
void mark_path(Map_Obj *map, int *path) {
    strcat(map->str_map, " [Path Marked]");
}

// Menyetel marker posisi awal
void set_start_pos_str_marker(int start_pos, char *themap) {
    strcat(themap, " [Start]");
}

// Menyetel marker posisi tujuan
void set_goal_pos_str_marker(int goal_pos, char *themap) {
    strcat(themap, " [Goal]");
}

// Menampilkan map ke layar
void show_map(Map_Obj *map) {
    printf("Map Details -> %s\n", map->str_map);
}

// Simulasi a_star dengan visualisasi (mengembalikan frame/gambar)
void a_star_with_visualization(Map_Obj *map) {
    printf("Menjalankan visualisasi eksplorasi untuk Task %d...\n", map->task_num);
    // Logika penyimpanan frame visualisasi ke file/memori
}

// Fungsi untuk menjalankan A* per task
void run_a_star_for_task(int task_num) {
    // Instantiate a map object for task
    Map_Obj task_map = create_map(task_num);
    
    // Run the A* algorithm and find the path
    int *path = a_star(&task_map);
    
    // Mark the path on the map
    mark_path(&task_map, path);
    
    // Add the start and goal positions to the map
    // Di C, kita manipulasi langsung string map di dalam struct
    set_start_pos_str_marker(task_map.start_pos, task_map.str_map);
    set_goal_pos_str_marker(task_map.goal_pos, task_map.str_map);
    
    show_map(&task_map);
}

// Fungsi untuk menjalankan A* dan membuat GIF (Simulasi di C)
void run_a_star_for_task_with_creation_of_gif(int task_num) {
    Map_Obj task_map = create_map(task_num);
    
    // Menjalankan visualisasi
    a_star_with_visualization(&task_map);
    
    // Placeholder pembuatan GIF di C (biasanya butuh library tambahan seperti ImageMagick atau pustaka C kustom)
    char filename[100];
    snprintf(filename, sizeof(filename), "docs/exploration_of_task_%d.gif", task_num);
    printf("GIF berhasil disimpan ke: %s (Simulasi)\n", filename);
}

int main() {
    int tasks = MAX_TASKS;
    
    printf("Running A* for the tasks...\n");
    for (int task = 1; task <= tasks; task++) {
        printf("Task %d:\n", task);
        run_a_star_for_task(task);
        printf("Completed task %d.\n\n", task);
    }
    
    // Input interaktif menggantikan input() Python
    char user_input[10];
    printf("Do you want to create GIFs for the exploration of the maps? (y/n): ");
    if (fgets(user_input, sizeof(user_input), stdin) != NULL) {
        // Hilangkan newline karakter (\n) dari input
        user_input[strcspn(user_input, "\n")] = 0;
        
        // Perhatikan logika kondisi disesuaikan dengan maksud script asli Python Anda
        if (strcmp(user_input, "y") == 0 || strcmp(user_input, "Y") == 0) {
            printf("Creating GIFs for the exploration of the maps...\n");
            for (int task = 1; task <= tasks; task++) {
                printf("Task %d:\n", task);
                run_a_star_for_task_with_creation_of_gif(task);
                printf("Created GIF for task %d.\n\n", task);
            }
        } else {
            printf("Pembuatan GIF dibatalkan.\n");
        }
    }

    return 0;
}