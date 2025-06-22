#1) Complete the menubar by adding other dropdown menus.
#This lesson provides more closure to menubar, progress bar, spinbox
import tkinter as tk

#create  window
window = tk.Tk()
window.title("Menu Demonstration")

#creating widgets
#Add Menubar
menubar = tk.Menu(window)
#adding file menu and commands
file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label="Open...", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label='Exit',command=window.destroy)

#Adding Edit menu and commands
edit = tk.Menu(menubar, tearoff=0)
edit.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find', command=None)
edit.add_command(label='File again', command=None)

# Adding Help Menu
help_ = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)
#view menu 
view = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='View', menu=view)
view.add_command(label='Zoom',command=None)
view.add_command(label='Status Bar', command=None)
view.add_command(label='World Wrap', command=None)

# display Menu
window.config(menu=menubar)
window.mainloop()

#2) Create an interface for a food delivery app which looks similar to the following.

