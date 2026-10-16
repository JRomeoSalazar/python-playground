# 🐍 hola-python

Un playground para practicar Python con ejercicios, experimentos y pequeños scripts.

![Python](https://img.shields.io/badge/python-3.12-blue)
![Licencia](https://img.shields.io/badge/licencia-por%20definir-lightgrey)

## 📖 Sobre el proyecto

Repositorio de práctica donde cada script aborda un único tema de Python, desde
variables y bucles hasta asincronía y peticiones HTTP. Está pensado para quien
está aprendiendo el lenguaje y quiere ejemplos cortos que pueda ejecutar y modificar.

## 🗂️ Estructura

```text
hola-python/
├── analizador/          # Paquete con utilidades de texto (utilidades.py)
├── asincronia.py        # asyncio y asyncio.gather
├── bucles.py            # Bucles
├── cadenas.py           # Cadenas de texto
├── clases.py            # Programación orientada a objetos
├── comprehensive_lists.py  # Comprensión de listas
├── condicionales.py     # Condicionales
├── entrada.py           # Entrada de datos del usuario
├── estructuras.py       # Estructuras de datos
├── functiones.py        # Funciones
├── hello.py             # Primer script
├── peticiones.py        # Peticiones HTTP con requests
├── textos.py            # Usa el paquete analizador
├── tipos.py             # Tipos de datos
├── variables.py         # Variables
└── requirements.txt     # Dependencias (pip)
```

## 🚀 Primeros pasos

Requisitos: Python 3.12 y `pip`.

```bash
git clone <url-del-repo>
cd <nombre-del-repo>
```

Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
```

Instala las dependencias y ejecuta un script de ejemplo:

```bash
pip install -r requirements.txt
python hello.py
```

## 🛠️ Cómo usarlo

Para añadir un ejercicio o experimento:

1. Crea un archivo `.py` en la raíz, con nombre corto, en minúsculas y con guiones bajos.
2. Dedícalo a **un solo tema**.
3. Mantén el script independiente: que se ejecute con `python <script>.py`.
4. Si necesitas código compartido, ponlo en un paquete como `analizador/` y
   ejecuta el script desde la raíz del repo.
5. Si añades una librería, actualiza `requirements.txt`.

Convenciones: código, identificadores y comentarios en español.

> `peticiones.py` necesita conexión a internet.

## 📚 Temas que se practican

- Variables y tipos de datos
- Condicionales y bucles
- Cadenas y entrada de datos
- Estructuras de datos y comprensión de listas
- Funciones
- Programación orientada a objetos
- Módulos y paquetes
- Asincronía con `asyncio`
- Peticiones HTTP a APIs

## 📄 Licencia

<licencia> (pendiente de definir; el repositorio aún no incluye un archivo `LICENSE`).
