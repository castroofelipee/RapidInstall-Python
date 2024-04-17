import tkinter as tk
from tkinter import ttk


def open_next_window():
    next_window = tk.Toplevel()
    next_window.title("Next Window")
    next_window.geometry("300x200")

    label = tk.Label(next_window, text="This is the Next Window")
    label.pack()

    next_window.mainloop()
