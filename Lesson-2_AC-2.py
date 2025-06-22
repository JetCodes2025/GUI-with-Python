import tkinter as tk
from tkinter import ttk
# Crete window to display widgets
window = tk.Tk()
#progress bar widget 
progress = ttk.Progressbar(window, orient="horizontal", 
                          length=100, mode='determinate')
#function responsible to update 
def bar():
    import time
    progress['value'] =20
    window.update_idletasks()
    time.sleep(1)

    progress['value']= 40
    window.update_idletasks()
    time.sleep(1)

    progress['value']= 50
    window.update_idletasks()
    time.sleep(1)

    progress['value']= 60
    window.update_idletasks()
    time.sleep(1)
        
    progress['value']= 80
    window.update_idletasks()
    time.sleep(1)

    progress['value']=100
progress.pack(pady=10)

#this button will start the progress bar 
tk.Button(window, text='Start', command=bar).pack(pady=10)
window.mainloop()