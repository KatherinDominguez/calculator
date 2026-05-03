

import sys
import os

# Agregar las rutas de los módulos al path
sys.path.append(os.path.join(os.path.dirname(_file_), 'app', 'view'))
sys.path.append(os.path.join(os.path.dirname(_file_), 'app', 'controllers'))
sys.path.append(os.path.join(os.path.dirname(_file_), 'model'))

from view import View
from calculator_controller import CalculatorController

def main():
    # Crear la vista
    view = View()
    
    # Crear el controlador con la vista
    controller = CalculatorController(view)
    
    # Conectar la vista con el controlador
    view.set_controller(controller)
    
    # Iniciar la aplicación
    view.start()

if __name__ == "__main__":
    main()
