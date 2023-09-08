from tkinter import *


def multiplyNumbers():
    res = int(e1.get()) * int(e2.get())
    myText.set(res)


master = Tk()
myText = StringVar()
Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=2, sticky=W)
Label(master, text="Result:").grid(row=4, sticky=W)
result = Label(master, text="", textvariable=myText).grid(row=4, column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=2, column=1)
def divideNumbers():
    res = int(e1.get()) / int(e2.get())
    myText.set(res)
def substractNumbers():
    res = int(e1.get()) - int(e2.get())
    myText.set(res)
def addNumbers():
    res = int(e1.get()) + int(e2.get())
    myText.set(res)


b = Button(master, text="/", command=divideNumbers)
b.grid(row=0, column=3, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
b = Button(master, text="+", command=addNumbers)
b.grid(row=1, column=3, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
b = Button(master, text="-", command=substractNumbers)
b.grid(row=2, column=3, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
b = Button(master, text="*", command=multiplyNumbers)
b.grid(row=3, column=3, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)



mainloop()