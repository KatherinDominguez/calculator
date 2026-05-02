from functools import partial
import tkinter as tk

root = tk.Tk()

value_screen = tk.StringVar(value="")


def set_screen_value(value):
    value_screen.set(value)

def update_screen_value(value):
    if value_screen.get() == "0" and value == 0:
        return
    elif value_screen.get()== "0":
        value_screen.set("")
    value_screen.set(value_screen.get()+ str(value))



def create_screen():
    label = tk.Label(root,textvariable=value_screen)
    label.grid(row=0,column=0,columnspan=3)

def create_buttons_number():
    for i in range(9):
        btn = tk.Button(root,text=i+1,command=partial(update_screen_value,i+1))
        btn.grid(row=i//3+1,column=i%3)
    btn = tk.Button(root,text=0,command=partial(update_screen_value,0))
    btn.grid(row=4,column=0)

def create_buttons_operators():
    btn_sum = tk.Button(root,text="+")
    btn_substract = tk.Button(root,text="-")
    btn_times = tk.Button(root,text="*")
    btn_divide = tk.Button(root,text="/")
    btn_equal = tk.Button(root,text="=")
    btn_sum_sub = tk.Button(root,text="+/-")

    btn_sum.grid(row=1,column=3)
    btn_substract.grid(row=2,column=3)
    btn_times.grid(row=3,column=3)
    btn_divide.grid(row=4,column=3)
    btn_sum_sub.grid(row=4,column=2)
    btn_equal.grid(row=3,column=4,rowspan=2)




create_screen()
create_buttons_number()
create_buttons_operators()


root.mainloop()


