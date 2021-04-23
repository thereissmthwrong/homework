import tkinter as tk

width = 500
height = 500
deltax = 500
deltay = 150

root = tk.Tk()
root.title('Slot machine')
root.geometry(f'{width}x{height}+{deltax}-{deltay}')

for i in range(2):
    root.grid_rowconfigure(i,  weight =1)
for i in range(2):
    root.grid_columnconfigure(i,  weight =1)

frame1 = tk.Frame(root, background='blue', padx=5, pady=5)
frame2 = tk.Frame(root, background='red', padx=5, pady=5)
frame3 = tk.Frame(root, background='green', padx=5, pady=5)
frame1.grid(row=0, column=0, sticky = tk.N + tk.W)
frame2.grid(row=0, column=1, sticky = tk.N + tk.E)
frame3.grid(row=1, column=0, columnspan=2, sticky = tk.S + tk.E + tk.W)

for i in range(2):
	frame1.grid_rowconfigure(i,  weight =1)
for i in range(2):
	frame1.grid_columnconfigure(i,  weight =1)
for i in range(2):
	frame2.grid_rowconfigure(i,  weight =1)
for i in range(2):
	frame2.grid_columnconfigure(i,  weight =1)
for i in range(2):
	frame3.grid_rowconfigure(i,  weight =1)
for i in range(2):
	frame3.grid_columnconfigure(i,  weight =1)

btn1 = tk.Button(frame1, text = 'BUTTON1')
btn2 = tk.Button(frame1, text = 'BUTTON2')
btn3 = tk.Button(frame1, text = 'BUTTON3')
btn1.grid(row=0, column=0, sticky = tk.N +tk.W)
btn2.grid(row=0, column=1, sticky = tk.N +tk.E)
btn3.grid(row=1, column=0, columnspan=2, sticky = tk.S +tk.E + tk.W)

btn4 = tk.Button(frame2, text = 'BUTTON4')
btn5 = tk.Button(frame2, text = 'BUTTON5')
btn6 = tk.Button(frame2, text = 'BUTTON6')
btn4.grid(row=0, column=0, sticky = tk.N +tk.W)
btn5.grid(row=0, column=1, sticky = tk.N +tk.E)
btn6.grid(row=1, column=0, columnspan=2, sticky = tk.S +tk.E + tk.W)

btn7 = tk.Button(frame3, text = 'BUTTON7')
btn8 = tk.Button(frame3, text = 'BUTTON8')
btn9 = tk.Button(frame3, text = 'BUTTON9')
btn7.grid(row=0, column=0, sticky = tk.N +tk.W)
btn8.grid(row=0, column=1, sticky = tk.N +tk.E)
btn9.grid(row=1, column=0, columnspan=2, sticky = tk.S +tk.E + tk.W)

root.mainloop()


