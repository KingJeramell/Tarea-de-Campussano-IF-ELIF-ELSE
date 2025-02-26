Salario = int(input("Inserte su salario mensual:"))
if Salario < 10000:
    impuesto = 0
elif Salario < 30000:
    impuesto = Salario * 0.10
else:
    impuesto = Salario * 0.20
Salario_final= Salario - impuesto
print(f"Impuesto aplicado: ${impuesto:.2f}")
print(f"Salario después del impuesto: ${Salario_final:.2f}")