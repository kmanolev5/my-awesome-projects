import tkinter

def dodajTextVoEntry(text):
    entry.insert(tkinter.END, text)

def calculate():
    str_to_calculate = str(entry.get())
    calc = eval(str_to_calculate)
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, calc)


screen = tkinter.Tk()
screen.title('Calculator')

screen.geometry("340x500")
screen.config(padx=20, pady=20)

entry = tkinter.Entry()
entry.config(width=20, font=("default", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5)

broj1 = tkinter.Button(screen, text="1", command=lambda: dodajTextVoEntry("1"))
broj1.grid(row=3, column=0)
broj1.config(width=5)

broj2 = tkinter.Button(screen, text="2", command=lambda: dodajTextVoEntry("2"))
broj2.grid(row=3, column=1)
broj2.config(width=5)

broj3 = tkinter.Button(screen, text="3", command=lambda: dodajTextVoEntry("3"))
broj3.grid(row=3, column=2)
broj3.config(width=5)

broj4 = tkinter.Button(screen, text="4", command=lambda: dodajTextVoEntry("4"))
broj4.grid(row=2, column=0)
broj4.config(width=5)

broj5 = tkinter.Button(screen, text="5", command=lambda: dodajTextVoEntry("5"))
broj5.grid(row=2, column=1)
broj5.config(width=5)

broj6 = tkinter.Button(screen, text="6", command=lambda: dodajTextVoEntry("6"))
broj6.grid(row=2, column=2)
broj6.config(width=5)

broj7 = tkinter.Button(screen, text="7", command=lambda: dodajTextVoEntry("7"))
broj7.grid(row=1, column=0)
broj7.config(width=5)

broj8 = tkinter.Button(screen, text="8", command=lambda: dodajTextVoEntry("8"))
broj8.grid(row=1, column=1)
broj8.config(width=5)

broj9 = tkinter.Button(screen, text="9", command=lambda: dodajTextVoEntry("9"))
broj9.grid(row=1, column=2)
broj9.config(width=5)

broj0 = tkinter.Button(screen, text="0", command=lambda: dodajTextVoEntry("0"))
broj0.grid(row=4, column=1)
broj0.config(width=5)

plus = tkinter.Button(screen, text="+", command=lambda: dodajTextVoEntry("+"))
plus.grid(row=4, column=3)
plus.config(width=5)

minus = tkinter.Button(screen, text="-", command=lambda: dodajTextVoEntry("-"))
minus.grid(row=3, column=3)
minus.config(width=5)

mnozi = tkinter.Button(screen, text="*", command=lambda: dodajTextVoEntry("*"))
mnozi.grid(row=2, column=3)
mnozi.config(width=5)

deli = tkinter.Button(screen, text="/", command=lambda: dodajTextVoEntry("/"))
deli.grid(row=1, column=3)
deli.config(width=5)

ednakvo = tkinter.Button(screen, text="=", command=calculate)
ednakvo.grid(row=5, column=3)
ednakvo.config(width=5)


## screen end
screen.mainloop()
