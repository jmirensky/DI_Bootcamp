# Ejercicio de módulos en Python – Paso a paso completo

Este documento explica **qué archivo va dónde**, **qué escribir en cada uno** y **qué hace cada línea**, sin asumir conocimientos previos.

---

## 0. Estructura del proyecto
Generar la carpeta modules_exercise


## 0.5. AMBIENTE VIRTUAL
👉 El .venv va en la carpeta raíz del proyecto, al mismo nivel que tus .py.

Abres la terminal y te parás en la carpeta de tu proyecto
Ejecutas:
    python -m venv .venv     #  creá un entorno virtual en la carpeta .venv
Resultado: se crea una carpeta .venv con su propia versión de Python y pip.

Activar el entorno virtual
    .venv\Scripts\activate

Una vez activado, se mostrará asi en la terminal:
    (.venv) C:\modules_exercise>

Ahora toca descargar 2 paquetes (faker = genera datos falsas y tabulate = arma tablas prolijas ) dentro de venv activo
en la terminal
pip install faker tabulate


## 2. Estructura del proyecto

Tu carpeta del proyecto debe verse así:

```
modules_exercise/
│
├── .venv/                 # Entorno virtual (no se toca)
├── create_files.py        # Script que genera datos falsos
├── main.py                # Script principal que procesa los datos
├── datefile1.txt          # Se crea automáticamente
├── datefile2.txt          # Se crea automáticamente
```

---

## 3. Archivo: `create_files.py`

Este archivo **solo sirve para generar datos**. 

### Código completo comentado

```python
from faker import Faker      # Importamos Faker para generar datos falsos

fake = Faker()               # Creamos un objeto Faker

def create_file(num):        # Función que crea un archivo de fechas
    # Abrimos (o creamos) un archivo en modo escritura
    # El nombre será datefile1.txt, datefile2.txt, etc.
    with open(f"datefile{num}.txt", "w") as f:            #with open(...) → forma correcta de leer archivos
        # Repetimos 100 veces
        for _ in range(100):
            # Escribimos una fecha falsa en cada línea
            f.write(fake.date() + "\n")


# Llamamos a la función dos veces para crear dos archivos
create_file(1)     # 100 fechas
create_file(2)     # 100 fechas
```

### Cómo se ejecuta

Desde la terminal (con el `.venv` activado):

```bash
python create_files.py
```

Resultado esperado:
- Se crean `datefile1.txt` y `datefile2.txt`
- No se imprime nada (esto es correcto)

---

## 4. Archivo: `main.py`

Este es el **programa principal**. El que procesa. Lee los archivos, muestra los datos y calcula la fecha mediana.

### Código completo comentado

```python
import sys                            # Para leer argumentos desde la terminal
from tabulate import tabulate         # Para mostrar datos en forma de tabla


def extract_file_contents(file_path):
    """
    Lee un archivo de texto y devuelve una lista de líneas limpias.
    """
    with open(file_path, "r") as f:               #with open(...) → forma correcta de leer archivos
        # Leemos cada línea, quitamos espacios y descartamos líneas vacías
        return [line.strip() for line in f if line.strip()]


def display_files(file1_contents, file2_contents):
    """
    Muestra el contenido de los dos archivos en formato de tabla.
    """
    table = {
        "file1": file1_contents,
        "file2": file2_contents
    }
    print(tabulate(table))


def main(file1, file2):
    # Leemos el contenido de cada archivo
    file1_data = extract_file_contents(file1)
    file2_data = extract_file_contents(file2)

    # Mostramos los datos en tabla
    display_files(file1_data, file2_data)

    # Unimos las fechas de ambos archivos, eliminamos duplicados y ordenamos
    dates = sorted(set(file1_data).union(file2_data))

    # Calculamos la fecha mediana
    print("\nFecha mediana:")
    print(dates[len(dates) // 2])


# Punto de entrada del programa
if __name__ == "__main__":            # ejecuta el código solo si el archivo es el principal
    # Verificamos que el usuario haya pasado exactamente 2 archivos
    if len(sys.argv) != 3:         #sys.argv → recibe archivos desde la terminal
        print("Usá: python main.py datefile1.txt datefile2.txt")
        sys.exit(1)

    # Ejecutamos la función principal con los archivos recibidos
    main(sys.argv[1], sys.argv[2])
```

---

## 5. Cómo se ejecuta `main.py`

Siempre desde la terminal:

```bash
python main.py datefile1.txt datefile2.txt
```

### Qué hace este comando

- `python main.py` → ejecuta el programa
- `datefile1.txt` → primer archivo de entrada
- `datefile2.txt` → segundo archivo de entrada

---

## 6. Ideas clave para estudiar (resumen realista)

- Cada archivo cumple **una sola función**
- `create_files.py` genera datos
- `main.py` procesa datos
- `sys.argv` permite pasar información desde la terminal
- El `.venv` vive en la raíz del proyecto y no se toca

---

## 8. Regla final
> En Python, debe existir **orden**
> Los módulos sirven para no escribir todo en un solo archivo, reutilizar código y mantener orden.
> El programa fue hecho para correrse desde la terminal, no con botón “Run” del editor

## 9. Salir del ambiente virtual.
(.venv) PS C:\Users\julie\01DI_Bootcamp\W3\day3\modules_excercise>   deactivate