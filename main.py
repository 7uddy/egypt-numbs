from tkinter import *
import tkinter.font as font
import customtkinter
from PIL import Image, ImageTk
import subprocess

customtkinter.set_appearance_mode("dark") 
root = customtkinter.CTk()
root.title('Calculator Egiptean - Meniu Principal')
root.geometry("500x350")
root.resizable(False, False)
root.iconbitmap('simboluri/favicon.ico')

image = Image.open('simboluri/background.png')
image = image.resize((650, 600))
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def ReprezintaGrafic():
	subprocess.run(["python", "reprezentare.py"])

def RealizeazaProdusul():
	subprocess.run(["python", "produs.py"])
	

def RealizeazaImpartirea():
	subprocess.run(["python", "impartire.py"])
	

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

button_ReprezentareGrafica = Button(root, text="REPREZENTARE GRAFICĂ", font = buttonFont, fg='white', padx=30, pady=30, borderwidth=2, activebackground='#ffdfba', bg='red', command=ReprezintaGrafic)
button_Inmultire = Button(root, text="PRODUSUL A DOUĂ NUMERE FOLOSIND ALGORITMUL EGIPTEAN", font=buttonFont, fg='white', padx=30, pady=30, borderwidth=2, activebackground='#ffdfba', bg='blue', command=RealizeazaProdusul)
button_Impartire = Button(root, text="ÎMPĂRȚIREA A DOUĂ NUMERE FOLOSIND ALGORITMUL EGIPTEAN", font=buttonFont, fg='white', padx=30, pady=30, borderwidth=2, activebackground='#ffdfba', bg='#e59b02', command=RealizeazaImpartirea)

button_ReprezentareGrafica.grid(row=0, pady = 20, padx=20, sticky='nsew')
button_Inmultire.grid(row=1, pady = 40, padx=20, sticky='nsew')
button_Impartire.grid(row=2, pady = 20, padx=20, sticky='nsew')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)

root.mainloop()

