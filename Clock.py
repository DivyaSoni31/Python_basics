from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %a') #%p for pm, %a for day, %b for month, %m for month,%j idk,%n bigger,%r 12h clock,
                                     #%t longer,%x for date,%y for year,%z idk
    label.config(text = string)
    label.after(1000, time)
    
label = Label(root, font=("ds-digital", 80),background= "black", foreground = "cyan")
label.pack(anchor= 'center')

time()
mainloop()
