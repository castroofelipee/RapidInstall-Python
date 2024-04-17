import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime


def log_message(action):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    message = f"{timestamp} {action}\n"
    return message


def next_action():
    # Abre a segunda janela ao clicar em "Next"
    import next_window

    next_window.open_next_window()


def cancel_action():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open("logs/logs.txt", "a") as arquivo:
        arquivo.write(log_message("Application canceled"))

    print("Application canceled")
    window.destroy()


# =================================== #
#             INTERFACE
# =================================== #
window = tk.Tk()
window.title("RapidInstall App")
window.geometry("500x300")

name_label = tk.Label(window, text="RapidInstall", font=("Arial", 14, "bold"))
name_label.pack()

powered_by_label = tk.Label(
    window, text="Powered by Felipe Castro ©", font=("Arial", 10, "bold")
)
powered_by_label.pack()

welcome_text = """
Welcome to the RapidInstall installer!
This open-source application makes it easy to install software on your computer.

System Requirements:
- RAM memory: 4 GB or more
- Disk space: 500 MB or more
"""

welcome_label = tk.Label(window, text=welcome_text, font=("Arial", 10), justify=tk.LEFT)
welcome_label.pack()

inferior_space = tk.Frame(window, height=50)
inferior_space.pack(fill=tk.X)

frame_button = tk.Frame(window)
frame_button.pack(side=tk.RIGHT, padx=20, pady=20)

button_next = ttk.Button(frame_button, text="Next", command=next_action)
button_next.pack(side=tk.LEFT, padx=6)

button_cancel = ttk.Button(frame_button, text="Cancel", command=cancel_action)
button_cancel.pack(side=tk.LEFT, padx=6)

window.mainloop()
