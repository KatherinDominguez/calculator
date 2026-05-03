import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from model import suma, resta, multiplicacion, division

class CalculatorController:
    def __init__(self, view):
        self.view = view
        self.current_input = ""
        self.first_number = None
        self.operator = None

    def process_input(self, value):
        if value in ("+", "-", "*", "/"):
            if self.current_input:
                self.first_number = float(self.current_input)
                self.operator = value
                self.current_input = ""
        elif value == "=":
            if self.first_number is not None and self.operator and self.current_input:
                second = float(self.current_input)
                try:
                    if self.operator == "+":
                        result = suma(self.first_number, second)
                    elif self.operator == "-":
                        result = resta(self.first_number, second)
                    elif self.operator == "*":
                        result = multiplicacion(self.first_number, second)
                    elif self.operator == "/":
                        result = division(self.first_number, second)
                    self.current_input = str(result)
                    self.view.set_screen_value(self.current_input)
                except ValueError as e:
                    self.view.set_screen_value("Error")
                    self.current_input = ""
                self.first_number = None
                self.operator = None
        elif value == "+/-":
            if self.current_input:
                self.current_input = str(float(self.current_input) * -1)
                self.view.set_screen_value(self.current_input)
        elif value == ".":
            if "." not in self.current_input:
                self.current_input += "."
                self.view.set_screen_value(self.current_input)
        else:
            self.current_input += str(value)
            self.view.set_screen_value(self.current_input)