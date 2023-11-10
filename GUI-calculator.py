# GUI- calculator.py
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() 
GUI.title('CALCULATOR FISH PRICE') # fish sell 39B per piece
GUI.geometry('500x300')

bg = PhotoImage(file= r'C:\Users\naphat.fueangfoo\OneDrive - Analog Devices, Inc\Desktop\python_file\car.png')
BG = Label(GUI, image = bg)
BG.pack()

L = Label(GUI, text='Please input the number of fish (kg)', font=(None,20))
L.pack()

v_quantity = StringVar() # for collecting string variable
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 39 
        messagebox.showinfo('Total price','Total price fish {} $'.format(calc))
        v_quantity.set('')
        E1.focus()
    except:
        messagebox.showwarning('Wrong Input', 'Enter only number')
        v_quantity.set('')


B = ttk.Button(GUI, text='Calculate',command=cal)
B.pack(ipadx=30,ipady=20)


GUI.mainloop()
