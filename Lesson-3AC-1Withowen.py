from tkinter import *

root=Tk()
root.geometry("300x150")

w=Label(root,text="Chocolates and Icecreams", font="50")
w.pack()

#first frame 
frame=Frame(root)
frame.pack()
#second frame 

bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

#adding button in first frame 
b1=Button(frame,text="Choco",fg="red",bg="beige")
b1.pack(side=LEFT)
b2=Button(frame,text="Dark Chocolates",fg="brown",bg="beige")
b2.pack(side=LEFT)
b3=Button(frame,text="White Chocolate",fg="orange",bg="beige")
b3.pack(side=LEFT)

#adding bottom frame 

b4=Button(bottom_frame,text="Vanilla ",fg="white",bg="red")
b4.pack(side=BOTTOM)
b5=Button(bottom_frame,text="Strawberry",fg="red",bg="pink")
b5.pack(side=BOTTOM)
b6=Button(bottom_frame,text="Butterscotch ",fg="white",bg="yellow")
b6.pack(side=BOTTOM)

root.mainloop()




