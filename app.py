import tkinter as tk
from datetime import datetime, timedelta

# Definições das Funções
def start():
    global running, start_time
    if not running:
        running = True
        start_time = datetime.now() - elapsed_time
        update_timer()

def stop():
    global running
    if running:
        running = False
        label.after_cancel(timer_id)

def reset():
    global elapsed_time, running
    running = False
    elapsed_time = timedelta()
    label.config(text="00:00:00.000")
    marks_label.config(text="")

def mark():
    if running:
        marks_label.config(text=marks_label['text'] + str(elapsed_time)[:-4] + '\n')

def update_timer():
    global elapsed_time, start_time, timer_id
    if running:
        elapsed_time = datetime.now() - start_time
        label.config(text=str(elapsed_time)[:-4])
        timer_id = label.after(10, update_timer)

# Configuração da Janela Tkinter
root = tk.Tk()
root.title("Cronômetro Estilizado")

# Estilização
root.configure(bg="#333")
root.geometry("500x250")

# Widgets
label = tk.Label(root, text="00:00:00.000", font=("Arial", 30), bg="#333", fg="white")
label.pack()

button_frame = tk.Frame(root, bg="#333")
button_frame.pack(expand=True)

start_button = tk.Button(button_frame, text="Iniciar", command=start, font=("Arial", 12), bg="#4CAF50", fg="white")
start_button.pack(side=tk.LEFT, padx=5, pady=5)

stop_button = tk.Button(button_frame, text="Parar", command=stop, font=("Arial", 12), bg="#f44336", fg="white")
stop_button.pack(side=tk.LEFT, padx=5, pady=5)

reset_button = tk.Button(button_frame, text="Resetar", command=reset, font=("Arial", 12), bg="#ff9800", fg="white")
reset_button.pack(side=tk.LEFT, padx=5, pady=5)

mark_button = tk.Button(button_frame, text="Marcar", command=mark, font=("Arial", 12), bg="#2196f3", fg="white")
mark_button.pack(side=tk.LEFT, padx=5, pady=5)

marks_label = tk.Label(root, text="", font=("Arial", 15), bg="#333", fg="white")
marks_label.pack(pady=5)

# Variáveis Globais
running = False
elapsed_time = timedelta()
start_time = None
timer_id = None

# Iniciar Loop Principal
root.mainloop()
