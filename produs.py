from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title('Produs')
root.geometry("800x200")
root.iconbitmap('simboluri/favicon.ico')
root.resizable(False, False)

image = Image.open('simboluri/backgroundProdus.png')
image = image.resize((1000, 650))
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

e1 = Entry(root, width=90, borderwidth=1, font='5')
e1.grid(row=0, column=0,columnspan=1, padx=30, pady=30)

e2 = Entry(root, width=90, borderwidth=1, font='5')
e2.grid(row=1, column=0, columnspan=1, padx=15, pady=15)

output = Entry(root, width=90, borderwidth=1, font='5')
output.config(state='disabled')
output.grid(row=3, column=0, columnspan=1, padx=15, pady=15)

def multiply_2_numbers(num1, num2):
    left_column = [num1]
    right_column = [num2]  
    while left_column[-1] > 1:
        left_column.append(left_column[-1] // 2)
    while len(right_column) < len(left_column):
        right_column.append(right_column[-1] * 2)
    product = 0
    for i, num in enumerate(left_column):
        if num % 2 == 1:
            product += right_column[i]
    return product

def numar_cifre_fractionar(numar):
    str_numar = str(numar)
    if '.' in str_numar:
        index_punct = str_numar.index('.') 
        numar_cifre_frac = len(str_numar) - index_punct - 1
        return numar_cifre_frac
    else:
        return 0

def FractionSplit(n, d):
    UnitFactions = []
    while (n > 0):
        x = (d + n - 1) // n
        s = "1/" + str(int(x))
        UnitFactions.append(s)
        n = n * x - d
        d = d * x
    return UnitFactions
 
def suma_fractii(numarator, numitor):
    def cmmdc(a, b):
        while b:
            a, b = b, a % b
        return a

    cmmdc_val = cmmdc(numarator, numitor)
    numarator //= cmmdc_val
    numitor //= cmmdc_val

    res = FractionSplit(numarator, numitor)
    
    return " + ".join(res)

def egyptian_multiplication(a, b):
    ParteIntreagaA = int(a)
    ParteIntreagaB = int(b)
    ParteFractionaraA = float(a) - int(a)
    ParteFractionaraB = float(b) - int(b)
    ParteFractionaraA = round(ParteFractionaraA,10000)
    ParteFractionaraB = round(ParteFractionaraB,10000)
    produs = 0
    if ParteFractionaraA != 0:
          numarCifreFractionaraA = numar_cifre_fractionar(ParteFractionaraA)
          numarCifreFractionaraB = numar_cifre_fractionar(ParteFractionaraB)
          produs+= multiply_2_numbers(ParteFractionaraA * pow(10,numarCifreFractionaraA), ParteIntreagaB) * pow(10,-numarCifreFractionaraA)
          produs+= multiply_2_numbers(ParteFractionaraA * pow(10,numarCifreFractionaraA), ParteFractionaraB * pow(10,numarCifreFractionaraB)) * pow(10,-numarCifreFractionaraA) * pow(10,-numarCifreFractionaraB) 
    if ParteIntreagaA != 0:
          numarCifreFractionaraB = numar_cifre_fractionar(ParteFractionaraB)
          produs+= multiply_2_numbers(ParteFractionaraB * pow(10,numarCifreFractionaraB), ParteIntreagaA) * pow(10,-numarCifreFractionaraB)
          produs+= multiply_2_numbers(ParteIntreagaA, ParteIntreagaB)
    parteFractionaraRezultat = round(float(produs) - int(produs),1000000)
    if(parteFractionaraRezultat == 0):  
        return int(produs)
    return str(int(produs)) + " + " + str(suma_fractii(parteFractionaraRezultat*pow(10,numar_cifre_fractionar(parteFractionaraRezultat)), pow(10,numar_cifre_fractionar(parteFractionaraRezultat))))

def Button_Equal():
	output.config(state='normal')
	output.delete(0, END)
	if len(e1.get()) == 0:
		output.config(state='disabled')
		return
	if len(e2.get()) == 0:
		output.config(state='disabled')
		return
	first_number = float(e1.get())
	second_number = float(e2.get())
	output.insert(0, egyptian_multiplication(first_number, second_number))
	output.config(state='disabled')


def Button_Clear1():
	e1.delete(0, END)
def Button_Clear2():
	e2.delete(0, END)

button_equal = Button(root, text="=", padx=5, pady=5, borderwidth=1, width=5, command=Button_Equal)
button_clear1 = Button(root, text="CLEAR", padx=5, pady=5, borderwidth=1, command=Button_Clear1)
button_clear2 = Button(root, text="CLEAR", padx=5, pady=5, borderwidth=1, command=Button_Clear2)

button_clear1.grid(row=0, column=3, columnspan=1)
button_clear2.grid(row=1, column=3, columnspan=1)
button_equal.grid(row=2, column=0, columnspan=1)


root.mainloop()

