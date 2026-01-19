#W3 D1 30 Dic 25
#Writing our own Modules = te importas clases y funciones que estan guardados en otro file separado

#tenes un proyecto/juego/desarrollo con clases y funciones
# 1° parte: 1 o varios files = modulos, con todas las lineas de codigo
# 2 la visualizacion (importas las clases y funciones de los primeros archivos)
#se mantiene todo "organizado"

# Almacenar tus funciones en un archivo separado permite:
    # reutilizar funciones en muchos programas diferentes
    # compartir archivos con otros programadores sin tener que compartir todo tu programa.

# Al importar funciones accedemos abibliotecas de funciones que ya han sido programadas x otros.

#Importación de funciones 
#los import van siempre arriba x convencion
    # from module_name import function_name
    # from module_name import function_0, function_1, function_2 as fun2

# uso de alias
# import random as rand
# import pandas as pd   --> util para data analytics

# #Exercise: # #Create a file called operators.py
# #Create 2 functions : addOperator(x,y) that returns the addition of 2 numbers,
#  and divideOperator(x,y) that returns the division of 2 numbers
# #Create another file called calculator.py, and import the operators module. Call the 2 functions and display the results
# importing specific functions and using alias
# from operators import addOperator as add, divideOperator as div
# print(add(10,2))  #12
# print(div(10,2))  #5

# -------

#Instalación de un módulo externo => con pip
#modulos que importamos de internet, de fuentes externas, de otros desarrolladores
# los de data analytics usaremos jupyter con frequencia
#python standard library, ej datetime = las debo importar para poder usarlas. Agregan peso al programa

#Buena práctica = usar ambientes virtuales y solo allí descargar librerias, según necesite mi proyecto en particular
# No los debo descargar en mi maquina en forma global
# Lo ambientes virtuales "encapsulan", "aislan" el proyecto, crean una pared entre la maquina y el proyecto.
# Para que los cambios de versiones de librerias no causen daño en el codigo

# Para mostrar mi proyecto en forma colaborativa a otros programadores (subir el código a GitHub),
# generaré y compartiré un requirements.txt., donde explicito los paquetes que usé.
# objetivo = facilitar a otros desarrolladores la instalación de las versiones correctas 
# del paquete de Python necesario para replicar mi proyecto.

# requirements.txt file se parece a esto:
# appnope==0.1.0
# backcall==0.1.0
# beautifulsoup4==4.6.3
# bleach==2.1.4
# certifi==2018.8.24
# chardet==3.0.4
# Click==7.0
# cycler==0.10.0
# decorator==4.3.0
# defusedxml==0.5.0
# entrypoints==0.2.3
# Flask==1.0.2

#en la terminal (no dentro de python) 
#check your pip installation:  --> python -m pip --version 
#ej--> pip 25.3 from C:\Users\......\Lib\site-packages\pip (python 3.14)

# pip freeze = veo todos los paquetes que ya tengo instalados

# Para instalar módulos:
    # $ pip install module_name 1 modulo en particular)
    # los modulos necesarios desde un archivo requirements.txt: pip install -r requirements.txt

# Para generar un archivo de requisitos para su proyecto de Python con pipreqs e instalarlo: $ pip install pipreqs

# Para generar un archivo de requisitos:
# $ pipreqs .
# $ pip freeze > requirements.txt   (forma alternativa, dentro de la carpeta de su proyecto)