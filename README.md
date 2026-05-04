# 🧮 Calculadora en Python

Proyecto de calculadora modular desarrollado en Python con arquitectura MVC. Incluye operaciones aritméticas básicas, interfaz gráfica con `tkinter`, menú interactivo en consola y pruebas unitarias.

## 📁 Estructura del proyecto

```
calculadora/
├── app/
│   ├── controllers/
│   │   ├── app_controller.py        # Conecta la vista con el modelo (GUI)
│   │   └── calculator_controller.py # Controlador con validaciones
│   ├── view/
│   │   └── view.py                  # Interfaz gráfica con tkinter
│   └── tests/
│       └── test_calculator.py       # Pruebas del controlador
├── model/
│   ├── __init__.py                  # Exporta las funciones del módulo
│   └── calculator.py                # Lógica de las operaciones
├── tests/
│   ├── test_calculadora.py          # Pruebas unitarias del modelo
│   └── README.md                    # Cómo correr las pruebas
├── main.py                          # Menú interactivo en consola
├── requirements.txt                 # Dependencias del proyecto
└── README.md
```

## ⚙️ Requisitos previos

- Python 3 instalado en tu sistema.
- `tkinter` incluido por defecto en Python 3 (no requiere instalación adicional).
- Estar ubicado en la raíz del proyecto (`calculadora/`).

## 🚀 Cómo ejecutar

### Opción 1 — Interfaz gráfica (GUI)

```bash
python -c "
import sys; sys.path.append('app/view'); sys.path.append('app/controllers')
from view import View
from app_controller import CalculatorController
v = View()
c = CalculatorController(v)
v.set_controller(c)
v.start()
"
```

Se abrirá una ventana con botones numéricos y operadores:

```
┌─────────────────┐
│       3.0       │  ← pantalla
├───┬───┬───┬───┬─┤
│ 1 │ 2 │ 3 │ + │*│
│ 4 │ 5 │ 6 │ - │/│
│ 7 │ 8 │ 9 │   = │
│ 0 │ . │+/-│     │
└───┴───┴───┴─────┘
```

### Opción 2 — Menú en consola

```bash
python main.py
```

```
===== Calculadora =====
1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir
=======================
```

## 🔢 Operaciones disponibles

| Operación      | Descripción                                     |
|----------------|-------------------------------------------------|
| Suma           | Retorna `a + b`                                 |
| Resta          | Retorna `a - b`                                 |
| Multiplicación | Retorna `a * b`                                 |
| División       | Retorna `a / b`. Lanza `ValueError` si `b == 0` |

## 🧪 Pruebas unitarias

```bash
python -m unittest discover tests
```

O para un archivo específico:

```bash
python -m unittest tests/test_calculadora.py
```

Consulta [`tests/README.md`](tests/README.md) para más detalles.

## 🛠️ Tecnologías

- Python 3
- `tkinter` — interfaz gráfica
- `unittest` — pruebas unitarias
- Arquitectura MVC (Modelo - Vista - Controlador)

## 👥 Contribuidores

- KatherinDominguez
- iangameplayhans
- maribelchoquemedrano02-beep
- EleonorAnturiano