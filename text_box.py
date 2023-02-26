from tkinter import *
 
from tkinter import messagebox
pencere = Tk()
 
pencere.title("Merhaba, nasilsin?")
pencere.geometry("420x210")

uygulama = Frame(pencere)
uygulama.grid()
 
L1 = Label(uygulama, text="Bir sey yazin")
L1.grid(padx=110, pady=10)
 
E1 = Entry(uygulama, bd=2)
E1.grid(padx=150, pady=5)

pencere.mainloop()
