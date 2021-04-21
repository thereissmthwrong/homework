import tkinter as tk
import random

def change_label():
    lb_text1.set(random.randrange(10))
    lb_text2.set(random.randrange(10))
    lb_text3.set(random.randrange(10))

width = 500
height = 500
deltax = 500
deltay = 150

root = tk.Tk()
root.title('Slot machine')
root.geometry(f'{width}x{height}+{deltax}-{deltay}')

lb_text1 = tk.StringVar()
lb_text2 = tk.StringVar()
lb_text3 = tk.StringVar()

lb1 = tk.Label(text = 'One', width = 2)
lb1.config(textvariable = lb_text1)
lb1.config(font=("Courier", 25))

lb2 = tk.Label(text = 'Two', width = 2)
lb2.config(textvariable = lb_text2)
lb2.config(font=("Courier", 25))

lb3 = tk.Label(text = 'Three', width = 2)
lb3.config(textvariable = lb_text3)
lb3.config(font=("Courier", 25))

lb_text1.set('x')
lb_text2.set('x')
lb_text3.set('x')

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=0, column=2)

btn1 = tk.Button(text = 'LET THE GAME BEGIN', command = change_label)
btn1.grid(row=1, column=0, columnspan=3)

root.mainloop()


