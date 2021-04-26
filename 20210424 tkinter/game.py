import tkinter as tk
from functools import partial
import random

el = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spoke')

def reset_st():
	played_sc.set(0)
	won_sc.set(0)
	lost_sc.set(0)
	err.set('')

def load_st(button):
	import os.path
	from os import path
	if path.exists('stats.txt'):
		f = open('stats.txt', 'r', encoding='utf-8')
		t = f.readlines()
		f.close()
		for i in range(len(t)):
			x = t[i].replace('\n','').split(': ')
			if x[0] == 'Games played':
				played_sc.set(int(x[1]))
			elif x[0] == 'Games won':
				won_sc.set(int(x[1]))
			elif x[0] == 'Games lost':
				lost_sc.set(int(x[1]))
	else:
		if button:
			err.set('The save file does not exist.')

def save_st():
	f = open('stats.txt', 'w', encoding='utf-8')
	f.write(f'Games played: {str(played_sc.get())}\nGames won: {str(won_sc.get())}\nGames lost: {str(lost_sc.get())}')
	f.close()
	err.set('')

def result(pc,user):
	played_sc.set(played_sc.get()+1)
	
	if pc == user:
		res.set('You neither won nor lost')
		res_lbl['foreground'] = 'blue'
	else:
		win = True
		#('0 Rock', '1 Paper', '2 Scissors', '3 Lizard', '4 Spoke')
		if pc == el[0] and (user == el[3] or user == el[2]):
			win = False
		elif pc == el[1] and (user == el[0] or user == el[4]):
			win = False
		elif pc == el[2] and (user == el[1] or user == el[3]):
			win = False
		elif pc == el[3] and (user == el[1] or user == el[4]):
			win = False
		elif pc == el[4] and (user == el[0] or user == el[2]):
			win = False
		
		if win:
			won_sc.set(won_sc.get()+1)
			res.set('You won')
			res_lbl['foreground'] = 'green'
		else:
			lost_sc.set(lost_sc.get()+1)
			res.set('You lost')
			res_lbl['foreground'] = 'red'

def ch_set(ch):
	ch_pc.set(random.choice(el))
	if ch == 'r':
		ch_user.set(el[0])
	elif ch == 'p':
		ch_user.set(el[1])
	elif ch == 's':
		ch_user.set(el[2])
	elif ch == 'liz':
		ch_user.set(el[3])
	elif ch == 'sp':
		ch_user.set(el[4])
	result(ch_pc.get(),ch_user.get())
	err.set('')

root = tk.Tk()
root.title('Rock Paper Scissors Lizard Spock')
root.geometry('510x490+500+150')
root.minsize(510, 490)
root.maxsize(510, 490)

game = tk.Frame(root, padx=50, pady=35)
game.grid(row=0, sticky = tk.N + tk.W)
stats = tk.Frame(root, padx=50)
stats.grid(row=1, sticky = tk.N + tk.W)

err = tk.StringVar()

#GAME ------------------------------------------------------------------

ch_pc = tk.StringVar()
ch_user = tk.StringVar()

pc_lbl = tk.Label(game)
ch_pc_lbl = tk.Label(game)
pc_lbl.config(text = 'PC:', font=("Helvetica", 20))
ch_pc_lbl.config(textvariable = ch_pc, font=("Helvetica", 20))

user_lbl = tk.Label(game)
ch_user_lbl = tk.Label(game)
user_lbl.config(text = 'USER:', font=("Helvetica", 20))
ch_user_lbl.config(textvariable = ch_user, font=("Helvetica", 20))

ch_pc.set('?')
ch_user.set('?')

pc_lbl.grid(row=0, column=0, sticky = tk.W)
user_lbl.grid(row=1, column=0, pady=10, sticky = tk.W)
ch_pc_lbl.grid(row=0, column=1, columnspan=4, sticky = tk.E)
ch_user_lbl.grid(row=1, column=1, pady=10, columnspan=4, sticky = tk.E)

rock_img = tk.PhotoImage(file = 'rock.png')
paper_img = tk.PhotoImage(file = 'paper.png')
scissors_img = tk.PhotoImage(file = 'scissors.png')
lizard_img = tk.PhotoImage(file = 'lizard.png')
spock_img = tk.PhotoImage(file = 'spock.png')

r_btn = tk.Button(game, text = 'Rock', image = rock_img, command = partial(ch_set,'r'))
p_btn = tk.Button(game, text = 'Paper', image = paper_img, command = partial(ch_set,'p'))
s_btn = tk.Button(game, text = 'Scissors', image = scissors_img, command = partial(ch_set,'s'))
liz_btn = tk.Button(game, text = 'Lizard', image = lizard_img, command = partial(ch_set,'liz'))
sp_btn = tk.Button(game, text = 'Spock', image = spock_img, command = partial(ch_set,'sp'))

r_btn.grid(row=2, column=0, padx=10, pady=10)
p_btn.grid(row=2, column=1, padx=10, pady=10)
s_btn.grid(row=2, column=2, padx=10, pady=10)
liz_btn.grid(row=2, column=3, padx=10, pady=10)
sp_btn.grid(row=2, column=4, padx=10, pady=10)

#RESULTS ---------------------------------------------------------------

res = tk.StringVar()

res_lbl = tk.Label(game)
res_lbl.config(textvariable = res, font=("Helvetica", 20))
res.set('')
res_lbl.grid(row=3, column=0, columnspan=5)

#STATS -----------------------------------------------------------------

played_sc = tk.IntVar()
won_sc = tk.IntVar()
lost_sc = tk.IntVar()

played_lbl = tk.Label(stats)
played_sc_lbl = tk.Label(stats)
played_lbl.config(text = 'Games played:', fg = 'gray', font=("Helvetica", 15))
played_sc_lbl.config(textvariable = played_sc, fg = 'gray', font=("Helvetica", 15))

won_lbl = tk.Label(stats)
won_sc_lbl = tk.Label(stats)
won_lbl.config(text = 'Games won:', fg = 'gray', font=("Helvetica", 15))
won_sc_lbl.config(textvariable = won_sc, fg = 'gray', font=("Helvetica", 15))

lost_lbl = tk.Label(stats)
lost_sc_lbl = tk.Label(stats)
lost_lbl.config(text = 'Games lost:', fg = 'gray', font=("Helvetica", 15))
lost_sc_lbl.config(textvariable = lost_sc, fg = 'gray', font=("Helvetica", 15))

reset_st()

played_lbl.grid(row=0, column=0, sticky = tk.W)
played_sc_lbl.grid(row=0, column=1, columnspan = 2, sticky = tk.E)

won_lbl.grid(row=1, column=0, sticky = tk.W)
won_sc_lbl.grid(row=1, column=1, columnspan = 2, sticky = tk.E)

lost_lbl.grid(row=2, column=0, sticky = tk.W)
lost_sc_lbl.grid(row=2, column=1, columnspan = 2, sticky = tk.E)

save_st_btn = tk.Button(stats, text = 'Save Stats', command = save_st)
save_st_btn.config(font=("Helvetica", 15))

load_st_btn = tk.Button(stats, text = 'Load Stats', command = partial(load_st, True))
load_st_btn.config(font=("Helvetica", 15))

reset_st_btn = tk.Button(stats, text = 'Reset Stats', command = reset_st)
reset_st_btn.config(font=("Helvetica", 15))

save_st_btn.grid(row=3, column=0, padx=10, pady=10)
load_st_btn.grid(row=3, column=1, padx=10, pady=10)
reset_st_btn.grid(row=3, column=2, padx=10, pady=10)

err_lbl = tk.Label(stats)
err_lbl.config(textvariable = err, fg = 'red', font=("Helvetica", 10))
err_lbl.grid(row=4, column=0, columnspan = 3, padx=10, pady=10)
err.set('')

load_st(False)

root.mainloop()
