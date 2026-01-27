
# Ejercicio práctico
# Crear un programa que genere carpetas:
# 5 carpetas principales: week1, week2, ..., week5
# Dentro de cada semana, 5 carpetas: day1, ..., day5
# Dentro de cada día, 2 carpetas: lesson y homework

import os

# Crear carpetas de semanas y días
for week in range(1, 6):  # week1 a week5
    week_folder = f"week{week}"
    os.makedirs(week_folder, exist_ok=True)  # crea la carpeta si no existe

    for day in range(1, 6):  # day1 a day5
        day_folder = os.path.join(week_folder, f"day{day}")
        os.makedirs(day_folder, exist_ok=True)

        # Dentro de cada día, crear lesson y homework
        os.makedirs(os.path.join(day_folder, "lesson"), exist_ok=True)
        os.makedirs(os.path.join(day_folder, "homework"), exist_ok=True)
