import numbers
import sys
import getopt
from tkinter import *
from tokenize import Floatnumber
from PIL import Image, ImageTk

root = Tk()
root.title('Reprezentarea grafica')
root.geometry("960x540")
root.iconbitmap('simboluri/favicon.ico')

max_symbols_per_row=17
button_frame = Frame(root)
button_frame.place(x=0, y=0)
image_frame = Frame(root)
image_frame.place(x=0, y=50)

e = Entry(button_frame, width=15, borderwidth=1)
e.pack(side=LEFT)
labels = []


def Button_Clear():
    global labels
    e.delete(0, END)
    for label in labels:
        label.grid_forget()
    labels = []

def NumImg(number,parteIntreaga=0):
    global labels
    int_number = int(number)
    to_divide = 1
    symbols_number = 0
    ok=0
    while int_number:
        if int_number%(to_divide*10)==0:
          to_divide*=10
          continue
        if int_number%to_divide==0 and to_divide!=1: 
            while int_number%to_divide==0 and int_number!=0 and int_number%(to_divide*10)!=0:
                symbols_number += 1
                int_number -= to_divide
        else:
            if to_divide == 1:
                while int_number and int_number%(to_divide*10)!=0:
                     symbols_number+=1
                     int_number-=1
        while symbols_number!=0:
          if to_divide==1:
              my_img = Image.open("simboluri/1.png")
              my_img = my_img.resize((10, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          elif to_divide==10:
              my_img = Image.open("simboluri/10.png")
              my_img = my_img.resize((50, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          elif to_divide==100:
              my_img = Image.open("simboluri/100.png")
              my_img = my_img.resize((50, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          elif to_divide==1000:  
              my_img = Image.open("simboluri/1000.png")
              my_img = my_img.resize((50, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          elif to_divide==10000:
              my_img = Image.open("simboluri/10000.png")
              my_img = my_img.resize((50, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          elif to_divide==100000:
              my_img = Image.open("simboluri/100000.png")
              my_img = my_img.resize((50, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          elif to_divide==1000000:
              my_img = Image.open("simboluri/1000000.png")
              my_img = my_img.resize((50, 46))
              my_img = ImageTk.PhotoImage(my_img)
              my_label = Label(image_frame,image=my_img)
              my_label.image = my_img
              labels.append(my_label)
          symbols_number-=1
         
        to_divide=to_divide*10
    to_divide=1
    aux_parte_intreaga=parteIntreaga
    while parteIntreaga:
        ok=1
        if parteIntreaga%(to_divide*10)==0:
          to_divide*=10
          continue
        if parteIntreaga%to_divide==0 and to_divide!=1: 
            while parteIntreaga%to_divide==0 and parteIntreaga!=0 and parteIntreaga%(to_divide*10)!=0:
                symbols_number += 1
                parteIntreaga -= to_divide
        else:
            if to_divide == 1:
                while parteIntreaga and parteIntreaga%(to_divide*10)!=0:
                     symbols_number+=1
                     parteIntreaga-=1
    aux_symbols_number=symbols_number
    parteIntreaga=aux_parte_intreaga
    for i, label in enumerate(labels):
        if parteIntreaga!=0:
            if symbols_number:
             row = i // max_symbols_per_row + 1
             column = i % max_symbols_per_row
             label.grid(row=row, column=column, padx=1, pady=1)
             symbols_number-=1
            else:
                if ok==1:
                    row = aux_symbols_number//max_symbols_per_row + 2
                    column = 0
                    label.grid(row=row, column=column, padx=1, pady=1)
                    ok=0
                else:
                    row = (i-aux_symbols_number-1) // max_symbols_per_row + 3 + aux_symbols_number//max_symbols_per_row + 2
                    column = (i-aux_symbols_number-1) % max_symbols_per_row
                    label.grid(row=row, column=column, padx=1, pady=1)
        else:
            row = i // max_symbols_per_row + 1
            column = i % max_symbols_per_row
            label.grid(row=row, column=column, padx=1, pady=1)
          

def numar_cifre_fractionar(numar):
    str_numar = str(numar)
    if '.' in str_numar:
        index_punct = str_numar.index('.') 
        numar_cifre_frac = len(str_numar) - index_punct - 1
        return numar_cifre_frac
    else:
        return 0

def NumberToImage(number):
    Button_Clear()
    numar = float(number)
    parteIntreaga = int(numar)
    NumImg(parteIntreaga)
    parteFractionara = numar % 1
    if parteFractionara != 0:
        my_img = Image.open("simboluri/punct.png")
        my_img = my_img.resize((50, 30))
        my_img = ImageTk.PhotoImage(my_img)
        my_label = Label(image_frame,image=my_img)
        my_label.image = my_img
        labels.append(my_label)
        NumImg(round(parteFractionara * pow(10, numar_cifre_fractionar(numar)),10),parteIntreaga)



button_clear = Button(button_frame, text="Clear", padx=5, pady=5, borderwidth=1, command=Button_Clear)
button_equal = Button(button_frame, text="=", padx=5, pady=5, borderwidth=1, command=lambda: NumberToImage(e.get()))

button_equal.pack(side=LEFT)
button_clear.pack(side=LEFT)


root.mainloop()

