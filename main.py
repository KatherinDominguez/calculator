import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.view.view import View
from app.controllers.calculator_controller import Controller

def main():
    view = View()
    controller = Controller(view)
    view.set_controller(controller)
    view.start()

if __name__ == "__main__":
    main()
