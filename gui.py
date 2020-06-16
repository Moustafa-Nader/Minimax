import tkinter as tk
import time
from state import *
window  = tk.Tk()
window.withdraw()

maxmvlabel = tk.Label(window,text="Max Moves")
maxmvlabel.grid(row = 0 , column = 0)
max_moves_widget = tk.StringVar()
maxmv = tk.Label(window , textvariable = max_moves_widget)
maxmv.grid(row =0, column = 1)

minsclabel = tk.Label(window,text="Min Score")
minsclabel.grid(row = 1 , column = 0)
min_score_widget = tk.StringVar()
minsc = tk.Label(window , textvariable = min_score_widget)
minsc.grid(row =1, column = 1)

maxdplabel = tk.Label(window,text="Max Depth")
maxdplabel.grid(row = 2 , column = 0)
max_depth_widget = tk.StringVar()
maxdp = tk.Label(window , textvariable = max_depth_widget)
maxdp.grid(row =2, column = 1)


maxsclabel = tk.Label(window,text="Max Score")
maxsclabel.grid(row = 6 , column = 0)
max_score_widget = tk.StringVar()
maxsc = tk.Label(window , textvariable = max_score_widget)
maxsc.grid(row =6, column = 1)

finalsclabel = tk.Label(window,text="Final Result")
finalsclabel.grid(row = 7 , column = 0)
final_score_widget = tk.StringVar()
finalsc = tk.Label(window , textvariable = final_score_widget)
finalsc.grid(row =7, column = 1)


result_widget = tk.StringVar()
result = tk.Entry(window , textvariable = result_widget,disabledbackground="grey",justify='center')
result.grid(row =8, column = 1)

b = [[0,0,0],[0,0,0],[0,0,0]]
t = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        t[i][j] = tk.StringVar()
for i in range(3):
    for j in range(3):
        b[i][j] = tk.Entry(window, textvariable=t[i][j],disabledbackground="white", disabledforeground="Black",font=('Helvetica','10'),state= 'disabled',justify='center')
        b[i][j].grid(row = i+3 , column = j,columnspan = 1)

def display_state(state):
    for i in range(3):
        for j in range(3):
            t[i][j].set(str(state.board[i][j]))

def win_display():
    result["disabledbackground"]="red"
    result["disabledforeground"]="white"
    result["font"] = ('Times','10')
    result["state"] ='disabled'
    result_widget.set(str("WINNER!"))


def fail_display():
    result["disabledbackground"]="black"
    result["disabledforeground"]="white"
    result["font"] = ('Times','10')
    result["state"] ='disabled'
    result_widget.set(str("FAIL!"))
 