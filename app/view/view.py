import tkinter as tk

root = tk.Tk()

value_screen = tk.StringVar(value="")

def create_screen():
    label = tk.Label(root,textvariable=value_screen)
    label.grid(row=0,column=0,columnspan=3)

def create_buttons_number():
    for i in range(9):
        btn = tk.Button(root,text=i+1)
        btn.grid(row=i//3+1,column=i%3)
    btn = tk.Button(root,text=0)
    btn.grid(row=4,column=0)

create_screen()
create_buttons_number()

root.mainloop()


