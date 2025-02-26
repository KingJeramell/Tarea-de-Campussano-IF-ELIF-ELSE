#Conversión de calificaciones
#Solicita la calificación numérica de un estudiante (0-100) y conviértela en una letra:
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#0-59: F
def convertir_calificacion():
    try:
        calificacion = int(input("Introduzca su calificación de un rango determinado desde (0-100): "))

        if 90 <= calificacion <= 100:
            letra = "A"
        elif 80 <= calificacion <= 89:
            letra = "B"
        elif 70 <= calificacion <= 79:
            letra = "C"
        elif 60 <= calificacion <= 69:
            letra = "D"
        elif 0 <= calificacion <= 59:
            letra = "F"
        else:
            print("Calificación fuera de rango.")
            return
        
        print(f"Felicitaciones su calificacion es: {letra}")

    except ValueError:
        print("Por favor, introduce un número válido.")