from view import View
from controller_original import CalculatorController

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