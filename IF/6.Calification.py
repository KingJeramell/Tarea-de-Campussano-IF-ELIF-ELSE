Calificaciones = int(input("Ingrese su calificacion:"))
if 0 < Calificaciones <= 100: #Verificacion de que el rango sea lo suficientemente valido
    if Calificaciones >=60:
        print(f"Felicidades has aprobado con un puntaje de {Calificaciones}")
    else:
        print("Lo siento has reprobado, necesitas mejorar sigue aprendiendo")
else:
    print("Error debe estar en un numero del 0 hasta el 100 no deben ser negativos los numeros")
