#What is the Season
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)


#month = int (input ('Enter a month: (1-12): '))
#if month in(3,4,5):
#     print("Spring")
#elif month in(6,7,8):
#     print("Summer")
#elif month in(9,10,11):
#     print("Autumn")
#elif month in(12,1,2):
#     print("Winter")
#else:
#     print('Invalid month')

#ESTA OPCION: validando el dato y repitiendo hasta que sea correcto.
while True:   # → sigue preguntando hasta que el usuario ingrese algo válido.
    month = int(input("Enter a month (1–12): "))

    if month < 1 or month > 12:
        print("Invalid month. Try again.")
        continue      #no sirve. Volvé arriba y empezá de nuevo (vuelve a input)

    if 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Autumn")
    else:
        print("Winter")

    break   #corta el loop solo cuando todo está bien.