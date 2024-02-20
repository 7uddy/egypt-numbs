from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title('Impartire')
root.geometry("500x200")
root.iconbitmap('simboluri/favicon.ico')
root.resizable(False, False)

image = Image.open('simboluri/backgroundImpartire.png')
image = image.resize((700, 550))
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

e1 = Entry(root, width=40, borderwidth=1, font='5')
e1.grid(row=0, column=0,columnspan=1, padx=30, pady=30)

e2 = Entry(root, width=40, borderwidth=1, font='5')
e2.grid(row=1, column=0, columnspan=1, padx=15, pady=15)

output = Entry(root, width=65, borderwidth=1, font='5')
output.config(state='disabled')
output.grid(row=3, column=0, columnspan=1, padx=15, pady=15)

def FractionSplit(n, d):
    UnitFactions = []
    while (n > 0):
        x = (d + n - 1) // n
        s = "1/" + str(x)
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

def division_2_numbers(a, b):
    if b == 0:
        return "NUL"
    rezultat = 0
    while a >= b:
        multiplier = 1
        while (b * multiplier) <= a:
            multiplier *= 2
        multiplier //= 2
        rezultat += multiplier
        a -= b * multiplier
    rest = a
    result_string = str(rezultat)
    if rest != 0:
        result_string = result_string + " + " + str(suma_fractii(int(rest),int(b)))
    return result_string

def egyptian_division(a, b):
    return division_2_numbers(a,b)

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
	output.insert(0, egyptian_division(first_number, second_number))
	output.config(state='disabled')


#def Button_Clear1():
#	e1.delete(0, END)
#def Button_Clear2():
#	e2.delete(0, END)

button_equal = Button(root, text="=", padx=5, pady=5, borderwidth=1, width=5, command=Button_Equal)

#button_clear1 = Button(root, text="CLEAR", padx=5, pady=5, borderwidth=1, command=Button_Clear1)
#button_clear2 = Button(root, text="CLEAR", padx=5, pady=5, borderwidth=1, command=Button_Clear2)
#button_clear1.grid(row=0, column=2, columnspan=1)
#button_clear2.grid(row=1, column=2, columnspan=1)
button_equal.grid(row=2, column=0, columnspan=1)


root.mainloop()

