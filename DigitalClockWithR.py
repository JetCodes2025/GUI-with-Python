import tkinter as tk
from time import strftime

#create window 
root=tk.Tk()
root.title("Digital Clock")

#function to update the time.

def time():
    string=strftime('%H:%M:%S %p') #12-hour format with AM/PM
    lbl.config(text=string) #update the label text
    lbl.after(1000,time) #Call the function again after 1 second

#create label 
lbl=tk.Label(root, font=("calibre", 40,"bold"),fg="green",bg="pink")
lbl.pack(anchor="center")
time()
root.mainloop()
