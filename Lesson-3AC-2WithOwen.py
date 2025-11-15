from tkinter import *
#create the window 
window=Tk()
window.title("My favorite Dishes")
window.geometry("300x250")
#create listbox object
scroll_bar=Scrollbar(window)
scroll_bar.pack(side=RIGHT, fill=Y)

listbox=Listbox(window,height=10,width=15,bg="grey",activestyle='dotbox',
                font="Arial",fg="yellow",yscrollcommand=scroll_bar.set)
label=Label(window,text="Food Items")

#enter the elements in the list 
listbox.insert(END,"Nachos")
listbox.insert(END,"Sandwich")
listbox.insert(END,"Burger")
listbox.insert(END,"Pizza")
listbox.insert(END,"French Fries")





# myList=Listbox(window,yscrollcommand=scroll_bar.set)
# for line in range(1,26):
#     myList.insert(END,"HI"+ str(line))
listbox.pack(side=LEFT, fill=BOTH)
scroll_bar.config(command=listbox.yview)

window.mainloop()