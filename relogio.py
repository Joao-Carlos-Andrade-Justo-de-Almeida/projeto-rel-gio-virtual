from tkinter import *
from time import strftime
from tkinter.ttk import *
window = Tk()
window.title('Relógio Digital')
def time():
    string = strftime('%H:%M:%S %p')
    relogio.config(text = string)
    relogio.after(1000, time)
relogio= Label(window, font=('Arial',40,'bold'),
               background='maroon',
               foreground='white')
relogio.pack(anchor='center')
time()
window.mainloop()
