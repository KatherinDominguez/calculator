# 🧮 Calculadora en Python

Proyecto de calculadora modular desarrollado en Python. Incluye operaciones aritméticas básicas, un menú interactivo en consola y pruebas unitarias.

## 📁 Estructura del proyecto

```
calculadora/
├── model/
│   ├── __init__.py        # Exporta las funciones del módulo
│   └── calculator.py      # Lógica de las operaciones
├── tests/
│   ├── __init__.py
│   ├── test_calculadora.py # Pruebas unitarias
│   └── README.md          # Cómo correr las pruebas
├── main.py                # Punto de entrada con menú interactivo
├── requirements.txt       # Dependencias del proyecto
└── README.md
```

## ⚙️ Requisitos previos

- Python 3 instalado en tu sistema.
- Estar ubicado en la raíz del proyecto (`calculadora/`).

## 🚀 Cómo ejecutar

```bash
python main.py
```

Verás un menú como este:

```
===== Calculadora =====
1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir
=======================
```

Elige una operación, ingresa dos números y obtén el resultado.

## 🔢 Operaciones disponibles

| Operación      | Descripción                                      |
|----------------|--------------------------------------------------|
| Suma           | Retorna `a + b`                                  |
| Resta          | Retorna `a - b`                                  |
| Multiplicación | Retorna `a * b`                                  |
| División       | Retorna `a / b`. Lanza `ValueError` si `b == 0`  |

## 🧪 Pruebas unitarias

Para ejecutar las pruebas:

```bash
python -m unittest tests/test_calculadora.py
```

O para descubrir todos los tests automáticamente:

```bash
python -m unittest discover tests
```

Consulta [`tests/README.md`](tests/README.md) para más detalles.

## 🛠️ Tecnologías

- Python 3
- Módulo estándar `unittest`
