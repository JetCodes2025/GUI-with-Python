 #in this activity we will use some more widgets which are used to make the application look better.
'''Examples 
1) Button
2) Entry for input field
3) Label
4) text
5) Text
6) Frame
7) Canvas
8) Listbox
9) Menu
'''
import tkinter as tk
window = tk.Tk()
window.title("Login Me")
window.geometry('400x300')
window.config(background='pink')
#label for user name
user_name = tk.Label(window,text="Username").place(x = 40, y = 60)
#label for password 
user_password = tk.Label(window, text="Password").place(x = 40, y= 100)
# button 
submit_button = tk.Button(window,text='Submit').place(x = 40, y = 130)
name_input_area = tk.Entry(window, width = 30).place(x = 110, y= 60)
password_input_area = tk.Entry(window,show="*", width=30).place(x = 110,y=100)


window.mainloop()


