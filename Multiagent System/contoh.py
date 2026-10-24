
import time

class SharedPath:
    def __init__(self):
        self.busy = False
        self.owner = None

    def request_path(self, robot_name):
        if not self.busy:
            self.busy = True
            self.owner = robot_name
            print(f"{robot_name}: Jalur tersedia, saya akan lewat.")
            return True
        else:
            print(f"{robot_name}: Jalur sedang digunakan oleh {self.owner}.")
            return False

    def release_path(self, robot_name):
        if self.owner == robot_name:
            self.busy = False
            self.owner = None
            print(f"{robot_name}: Barang berhasil diambil, jalur dilepaskan.")


class RobotAgent:
    def __init__(self, name, shared_path):
        self.name = name
        self.shared_path = shared_path

    def perform_task(self):
        print(f"\n{self.name} ingin mengambil barang.")

        if self.shared_path.request_path(self.name):
            print(f"{self.name} sedang melewati jalur...")
            print(f"{self.name} berhasil mengambil barang!")
            self.shared_path.release_path(self.name)
        else:
            print(f"{self.name} menunggu giliran.")


# Membuat lingkungan dan dua agen
path = SharedPath()

robot1 = RobotAgent("Robot 1", path)
robot2 = RobotAgent("Robot 2", path)

# Simulasi kedua robot
robot1.perform_task()
robot2.perform_task()
