import tkinter as tk
from time import strftime

#window
root = tk.Tk()
root.title("Menu Demonstration")
#create menubar 
menubar= tk.Menu(root)
#adding file menu 
file= tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file) #add that submenu to the menubar.
#add items/options inside the file menu
file.add_command(label='New',command=None)
file.add_command(label='Open',command=None)
file.add_command(label='Save',command=None)
file.add_separator() #draws horizontal divider line.
file.add_command(label='Exit',command=root.destroy)

root.config(menu=menubar)
root.mainloop()
