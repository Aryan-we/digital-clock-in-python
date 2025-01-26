#to create GUI interface
from tkinter import *
from time import strftime
def timer():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,timer)
#object root of Tk class
root=Tk()
#creating title
root.title("Digital Clock")
#creating a label to display the time,Label class is used
label=Label(root,font=("ds-digital",80),bg="black",fg='red')# fg is text color
label.pack(anchor="center")
timer()
#keep window in a loop
root.mainloop()