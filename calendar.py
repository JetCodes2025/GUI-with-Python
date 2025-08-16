# import all the methods and classes from tkinter 
from tkinter import *
#import calendar module
import calendar
def showCal():
    window=Tk()
    window.configure(background="white") 
    window.title("Calendar") #title of the screen 
    window.geometry("500x600") #setting the screen size#get methods to fetch the current year.
    
    fetch_year = int(year_field.get())

    #calendar method to get calendar in return .
    cal_content=calendar.calendar(fetch_year)
    
    #label for showing the content of the year 
    cal_year= Label(window,text=cal_content, font=("Courier New", 10))
    #grid to show the dates 
    cal_year.grid(row=5, column=1, padx=20)

#Driver code 
if __name__ =='__main__':
    new_window= Tk()
    
    #set bgcolor
    new_window.config(background = "white")
    new_window.title("Calendar ")
    new_window.geometry('250x140')
    cal = Label(new_window, text="Calendar",bg="dark gray",font=('roboto',28,'bold'))
    #create a label to enter year 
    year =Label(new_window,text="Enter Year ",bg="light green")

      #enter a text entry box 
    year_field=Entry(new_window)

    #create a show calendar button and call the function showCal()
    Show=Button(new_window,text="Show Calendar", fg="Green", bg="Red", command=showCal)
    Exit=Button(new_window,text="Exit",fg="Black",bg="Red", command=new_window.destroy)
    #arrange the widgets 
    cal.grid(row=1, column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    Show.grid(row=4,column=1)
    Exit.grid(row=7,column=1)

    #keep the window open 
    new_window.mainloop()


  

    



