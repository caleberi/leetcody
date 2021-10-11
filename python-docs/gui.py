import sys
from tkinter import *

main_window = Tk()
count_label = Label(main_window,text="Count: 0")
count_label.grid(row=0,column=1)
count_value = 0

def decrement_count():
    global count_value,count_label
    count_value = count_value+1
    count_label.configure("text=Count:" + str(count_value))

incr_btn = Button(main_window,text="Increment",command=decrement_count)
incr_btn.grid(row=0,column=0)
quit_btn = Button(main_window,text="Quit",command=main_window.destroy)
quit_btn.grid(row=1,column=1)
mainloop() 