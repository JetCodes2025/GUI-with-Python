import tkinter as tk
#create a window 
window = tk.Tk()
window.title("Menu Demonstration")
#create widgets 
menubar = tk.Menu(window)
#adding menu items
#adding file menu and command
file = tk.Menu(menubar,tearoff=0) 
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label = 'New File', command = None)
file.add_command(label='Open', command = None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit',command=window.destroy)
#attach the menubar to teh window to display the menu items in the window.
window.config(menu=menubar)

window.mainloop()




