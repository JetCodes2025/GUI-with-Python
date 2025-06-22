import tkinter as tk
master = tk.Tk()

window = tk.Spinbox(master, from_=0, to =10)
window.pack()

tk.mainloop()