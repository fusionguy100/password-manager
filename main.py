import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height = 200, width = 200)
canvas.create_image(100,100,image=logo_img)
canvas.pack()





tkinter.mainloop()