#this lession introduces you to tkinter library that help you to create desktop applications.
import  tkinter as tk 
#refer to tkinter elements like this 
#create a tkinter window 
root = tk.Tk()
#open window having dimension 200  x 200 
root.geometry('200x200')
#create a button 
btn = tk.Button(root,text = "Click Me!!",bd='5',background='blue',command=root.destroy)

#set the position of the button at the top of the window.
btn.pack(side = 'top')
root.mainloop()


