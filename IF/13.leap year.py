Año = int(input("Escribe un año "))
if (Año % 4 == 0 and Año % 100 !=0) or (Año % 400 == 0):
    print(f"El año {Año} es bisesto")
else:
    print(f"El año no es bisiesto lamentablemente")