from functools import partial
import tkinter as tk

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.value_screen = tk.StringVar(value="")

    def set_screen_value(self,value):
        self.value_screen.set(value)

    def update_screen_value(self,value):
        if self.value_screen.get() == "0" and value == 0:
            return
        elif self.value_screen.get()== "0":
            self.value_screen.set("")
        self.value_screen.set(self.value_screen.get()+ str(value))

    def create_screen(self):
        label = tk.Label(self.root,textvariable=self.value_screen)
        label.grid(row=0,column=0,columnspan=3)

    def create_buttons_number(self):
        for i in range(9):
            btn = tk.Button(self.root,text=i+1,command=partial(self.update_screen_value,i+1))
            btn.grid(row=i//3+1,column=i%3)
        btn = tk.Button(self.root,text=0,command=partial(self.update_screen_value,0))
        btn.grid(row=4,column=0)

    def create_buttons_operators(self):
        btn_sum = tk.Button(self.root,text="+")
        btn_substract = tk.Button(self.root,text="-")
        btn_times = tk.Button(self.root,text="*")
        btn_divide = tk.Button(self.root,text="/")
        btn_equal = tk.Button(self.root,text="=")
        btn_sum_sub = tk.Button(self.root,text="+/-")

        btn_sum.grid(row=1,column=3)
        btn_substract.grid(row=2,column=3)
        btn_times.grid(row=1,column=4)
        btn_divide.grid(row=2,column=4)
        btn_sum_sub.grid(row=4,column=2)
        btn_equal.grid(row=3,column=3,rowspan=2,columnspan=2)

    def create_buttton_decimal(self):
        btn_decimal = tk.Button(self.root,text=".")
        btn_decimal.grid(row=4,column=1)


    def start(self):
        self.create_screen()
        self.create_buttons_number()
        self.create_buttton_decimal()
        self.create_buttons_operators()


        self.root.mainloop()

