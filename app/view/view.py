import tkinter as tk

root = tk.Tk()

def create_buttons_number():
    for i in range(9):
        btn = tk.Button(root,text=i+1)
        btn.grid(row=i//3+1,column=i%3)
    btn = tk.Button(root,text=0)
    btn.grid(row=4,column=0)

create_buttons_number()

root.mainloop()


