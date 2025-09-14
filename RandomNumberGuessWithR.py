import tkinter as tk
import tkinter.messagebox
import random

#create window 
root=tk.Tk()
root.minsize(350,260)
root.title("Guess the number game: ")

#game logic
#generate random number between 1-20
number=random.randint(1,20)

#create a function to check the guess.
def check_num():
    guess=text_guess.get()
    guess=int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("high","Your guess is too high")
    elif guess < number:
        tkinter.messagebox.showinfo("low","Your guess is low")
    else:
        tkinter.messagebox.showinfo("good","Good job!!")
#config the name 
def btn_confirm():
    myName=text_name.get()
    tkinter.messagebox.showinfo("name", "Well," + myName + "I am thinking of number between 1 to 20")

# ------ GUI components -- 
#welcome label 
label = tk.Label(root,text="Welcome!!!!!!")
label.pack()
# name label 
label_name = tk.Label(root,text="What is your name? ")
label_name.place(x=10,y=60)
text_name=tk.Entry(root,width=20)
text_name.place(x=10, y=90)

#OK button 
btnOK=tk.Button(root,text="OK",command=btn_confirm)
btnOK.place(x = 200, y= 90,height = 28)

#guess input 
label_guess=tk.Label(root,text="Take a guess: ")
label_guess.place(x=10, y=150)
text_guess=tk.Entry(root,width=10)
text_guess.place(x=90,y=150)

#guess button 
btnCheck=tk.Button(root, text="Guess",command=check_num)
btnCheck.place(x = 200, y=150)

#run tkinter loop
root.mainloop()

    
    
