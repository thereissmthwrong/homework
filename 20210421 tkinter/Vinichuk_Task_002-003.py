import tkinter as tk
import re

def get_pass():
	if p.get() == '':
		err.set('The password cannot be empty!')
	else:
		print(p.get())

def countdown(count):        
    label['text'] = f'This window will be closed in {str(count)} seconds.'
    if count > 0:
        root.after(1000, countdown, count-1)

width = 500
height = 250
deltax = 500
deltay = 300

root = tk.Tk()
root.title('Slot machine')
root.geometry(f'{width}x{height}+{deltax}-{deltay}')
root.after(30000, lambda: root.destroy())

frame = tk.Frame(root, padx=25, pady=50)
frame.grid(row=0, column=0, sticky = tk.N + tk.W)

p = tk.StringVar()
err = tk.StringVar()

inpt = tk.Entry(frame, textvariable = p)
lbl = tk.Label(frame, )
lbl.config(textvariable = err, foreground = 'red')
btn = tk.Button(frame, text = 'Confirm the Password', command = get_pass)
inpt.grid(row=0, column=0, padx=25, sticky = tk.E + tk.W)
lbl.grid(row=1, column=0, padx=25, sticky = tk.E + tk.W)
btn.grid(row=2, column=0, padx=25, sticky = tk.E + tk.W)

err.set('')

label = tk.Label(frame)
label.grid(row=3, column=0, padx=25, sticky = tk.E + tk.W)
label.config(foreground = 'gray')

countdown(30)

root.mainloop()

