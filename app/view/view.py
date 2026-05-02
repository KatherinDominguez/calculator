from functools import partial
import tkinter as tk

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.value_screen = tk.StringVar(value="")
        self.controller = None

    def set_controller(self,controller):
        self.controller = controller

    def button_click(self,value):
        self.controller.process_input(value)

    def set_screen_value(self,value):
        self.value_screen.set(value)

    def create_screen(self):
        label = tk.Label(self.root,textvariable=self.value_screen)
        label.grid(row=0,column=0,columnspan=3)

    def create_buttons_number(self):
        for i in range(9):
            btn = tk.Button(self.root,text=i+1,command=partial(self.button_click,i+1))
            btn.grid(row=i//3+1,column=i%3)
        btn = tk.Button(self.root,text=0,command=partial(self.button_click,0))
        btn.grid(row=4,column=0)

    def create_buttons_operators(self):
        btn_sum = tk.Button(self.root,text="+",command=partial(self.button_click,"+"))
        btn_substract = tk.Button(self.root,text="-",command=partial(self.button_click,"-"))
        btn_times = tk.Button(self.root,text="*",command=partial(self.button_click,"*"))
        btn_divide = tk.Button(self.root,text="/",command=partial(self.button_click,"/"))
        btn_equal = tk.Button(self.root,text="=",command=partial(self.button_click,"="))
        btn_sum_sub = tk.Button(self.root,text="+/-",command=partial(self.button_click,"+/-"))

        btn_sum.grid(row=1,column=3)
        btn_substract.grid(row=2,column=3)
        btn_times.grid(row=1,column=4)
        btn_divide.grid(row=2,column=4)
        btn_sum_sub.grid(row=4,column=2)
        btn_equal.grid(row=3,column=3,rowspan=2,columnspan=2)

    def create_buttton_decimal(self):
        btn_decimal = tk.Button(self.root,text=".",command=partial(self.button_click,"."))
        btn_decimal.grid(row=4,column=1)


    def start(self):
        self.create_screen()
        self.create_buttons_number()
        self.create_buttton_decimal()
        self.create_buttons_operators()


        self.root.mainloop()
view = View()
view.start()
