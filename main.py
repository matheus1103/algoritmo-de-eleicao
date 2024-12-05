import tkinter as tk
import random
import time
import threading
import math

# Classe para simular o processo de eleição em anel.
class RingElectionSimulator:
    def __init__(self, root, num_processes):
        self.root = root
        self.num_processes = num_processes
        self.processes = [i for i in range(num_processes)]
        self.active_processes = [True] * num_processes
        self.coordinator = None
        self.canvas = tk.Canvas(root, width=900, height=600, bg="white")
        self.canvas.pack()
        self.logs = []
        self.draw_ring()
        self.start_button = tk.Button(root, text="Start Election", command=self.start_election_thread)
        self.start_button.pack()
        self.fail_button = tk.Button(root, text="Fail Random Process", command=self.fail_random_process)
        self.fail_button.pack()

    # Função para desenhar o anel de processos na tela.
    def draw_ring(self):
        self.canvas.delete("all")
        radius = 200
        center_x, center_y = 450, 300
        angle_step = 360 / self.num_processes
        self.positions = []
        for i in range(self.num_processes):
            angle = angle_step * i
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))
            self.positions.append((x, y))
            color = "green" if self.active_processes[i] else "red"
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)
            text = f"{i}"
            if i == self.coordinator:
                text += f" (Líder)"
            self.canvas.create_text(x, y, text=text, font=("Arial", 14))
            # Display logs below each process
            if i < len(self.logs):
                self.canvas.create_text(x, y + 30, text=self.logs[i], font=("Arial", 10), fill="blue")

    def start_election_thread(self):
        """
        Inicia uma nova thread para executar o processo de eleição.
        """
        threading.Thread(target=self.start_election, daemon=True).start()

    def start_election(self):
        """
        Executa o processo de eleição em anel, escolhendo um iniciador aleatório e determinando o novo coordenador.
        """
        initiator = random.choice([i for i in range(self.num_processes) if self.active_processes[i]])
        self.log_message(f"Process {initiator} iniciou a eleição.", initiator)
        current = initiator
        election_message = [initiator]
        visited = set()
        while True:
            time.sleep(1)
            next_process = (current + 1) % self.num_processes
            while not self.active_processes[next_process]:
                next_process = (next_process + 1) % self.num_processes
            election_message.append(next_process)
            self.log_message(f"Processo {current} -> {next_process} IDs: {election_message}.", current)
            visited.add(next_process)
            if next_process == initiator or len(visited) == self.num_processes:
                break
            current = next_process
        highest_id = max(election_message)
        self.coordinator = highest_id
        self.log_message(f"Processo {highest_id} lider.", highest_id)
        self.announce_coordinator(highest_id, initiator)
        self.draw_ring()

    def announce_coordinator(self, coordinator, initiator):
        current = initiator
        visited = set()
        while True:
            time.sleep(2)
            next_process = (current + 1) % self.num_processes
            while not self.active_processes[next_process]:
                next_process = (next_process + 1) % self.num_processes
            self.log_message(f"Processo {current} -> {next_process} lider: {coordinator}.", current)
            visited.add(next_process)
            if next_process == initiator or len(visited) == self.num_processes:
                break
            current = next_process

    def fail_random_process(self):
        """
        Marca um processo aleatório como falho e inicia uma nova eleição se o coordenador falhar.
        """
        active_processes = [i for i in range(self.num_processes) if self.active_processes[i]]
        if active_processes:
            failed_process = random.choice(active_processes)
            self.active_processes[failed_process] = False
            self.log_message(f"Processo {failed_process} falhou.", failed_process)
            self.draw_ring()
            self.start_election_thread()

    def log_message(self, message, process_id=None):
        print(message)
        if process_id is not None:
            if len(self.logs) <= process_id:
                self.logs.extend([""] * (process_id - len(self.logs) + 1))
            self.logs[process_id] = message
        self.root.after(0, lambda: self.root.title(message))
        self.draw_ring()

def main():
    """
    Função principal para inicializar a interface e executar o simulador de eleição em anel.
    """
    root = tk.Tk()
    root.title("Simulador de Eleição em Anel")
    simulator = RingElectionSimulator(root, num_processes=8)
    root.mainloop()

if __name__ == "__main__":
    main()
