from main import implement
from tkinter import *

import re

master = Tk()
master.title("Daily Horoscope")
master.geometry("700x400")


def scraping():
    zsign = zodiac.get()
    l = implement(zsign)

    label1 = Label(text="Your horoscope is "+l[0],bg="blue",fg="white")
    label1.pack()

    label2 = Label(text="Today's date is "+l[1],fg="white",bg="orange")
    label2.pack()

    horoscope = l[2].split('.')
    label=[]
    for i in horoscope:
        label3 = Label(text=i,bg="purple",fg="white")
        label3.pack()


label = Label(text="Enter your zodiac sign ",fg="white",bg="orange")
label.pack()

zodiac = StringVar()

entry = Entry(textvariable=zodiac)
entry.pack()

print(entry.get())



b = Button(text="Enter", command=scraping,fg="white",bg="red")
b.pack()






master.mainloop()