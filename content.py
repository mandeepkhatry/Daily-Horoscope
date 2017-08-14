from main import implement
from tkinter import *

import re

master = Tk()
master.title("Daily Horoscope")
master.geometry("1200x500")


def scraping():
    zsign = zodiac.get()
    l = implement(zsign)

    label1 = Label(text="Your horoscope is "+l[0],bg="blue",fg="white", font=("Helvetica", 14))
    label1.pack()

    label2 = Label(text="Today's date is "+l[1],fg="white",bg="orange", font=("Helvetica", 12))
    label2.pack()

    horoscope = l[2].split('.')
    label=[]
    for i in horoscope:
        label3 = Label(text=i,bg="purple",fg="white", font=("Helvetica", 14))
        label3.pack()


label = Label(text="Enter your zodiac sign ",fg="white",bg="orange", font=("Helvetica", 14))
label.pack()

zodiac = StringVar()

entry = Entry(textvariable=zodiac, font=("Helvetica", 14))
entry.pack()

print(entry.get())



b = Button(text="Enter", command=scraping,fg="white",bg="red", font=("Helvetica", 14))
b.pack()






master.mainloop()
