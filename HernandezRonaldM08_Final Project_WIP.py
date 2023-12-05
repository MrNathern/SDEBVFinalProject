import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("To-do List")
root.geometry("750x640")

title_label = tk.Label(root, 
                       text="Daily Tasks",
                       font="Ariel 30",
                       padx=10,
                       pady=20)
title_label.pack()

container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(1):
    ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()



