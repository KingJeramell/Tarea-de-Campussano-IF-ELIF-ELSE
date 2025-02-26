#Comparación de tres longitudes
#Solicita tres números que representan longitudes y determina si pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero).
a = int(input("introduzca su primera longitud"))
b = int(input("introduzca su segunda longitud"))
c = int(input("introduzca su tercera longitud"))

if a + b > c and a + c > b and b + c > a:
    print("Las longitudes pueden formar un triangulo.")
else:
    print("Las longitudes NO pueden formar un triangulo.")