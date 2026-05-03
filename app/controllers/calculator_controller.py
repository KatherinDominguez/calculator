from model.calculator import suma, resta, multiplicacion, division

class Controller:
    def __init__(self, view):
        self.view = view
        self.current_value = "0"
        self.previous_value = None
        self.operator = None
        self.reset_screen = False
        self.view.set_screen_value(self.current_value)

    def process_input(self, value):
        value_str = str(value)

        if value_str in "0123456789.":
            if self.reset_screen:
                self.current_value = value_str
                self.reset_screen = False
            else:
                if self.current_value == "0" and value_str != ".":
                    self.current_value = value_str
                else:
                    self.current_value += value_str
            self.view.set_screen_value(self.current_value)

        elif value_str in ["+", "-", "*", "/"]:
            if self.operator and not self.reset_screen:
                self.calculate()
            self.previous_value = self.current_value
            self.operator = value_str
            self.reset_screen = True

        elif value_str == "=":
            if self.operator:
                self.calculate()
                self.operator = None
                self.reset_screen = True
        
        elif value_str == "+/-":
            if self.current_value != "0" and self.current_value != "Error":
                if self.current_value.startswith("-"):
                    self.current_value = self.current_value[1:]
                else:
                    self.current_value = "-" + self.current_value
                self.view.set_screen_value(self.current_value)

    def calculate(self):
        try:
            a = float(self.previous_value)
            b = float(self.current_value)
            
            if self.operator == "+":
                res = suma(a, b)
            elif self.operator == "-":
                res = resta(a, b)
            elif self.operator == "*":
                res = multiplicacion(a, b)
            elif self.operator == "/":
                res = division(a, b)
                
            if isinstance(res, float) and res.is_integer():
                res = int(res)
                
            self.current_value = str(res)
            self.view.set_screen_value(self.current_value)
        except Exception:
            self.current_value = "Error"
            self.view.set_screen_value(self.current_value)
