#Operadores

print("Comparación de números\n")
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))

if num1 > num2:
    print("El número mayor es: " + str(num1))
elif num1 < num2:
    print("El número mayor es: " + str(num2))
else:
    print("Los valores son iguales.")