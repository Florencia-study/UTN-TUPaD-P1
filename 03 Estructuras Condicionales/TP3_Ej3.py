#Ej 3. El programa permite solo ingresar números pares.

numero = int (input("Ingrese un número par: "))

#condicion que evalua si el numero es par o impar. Invalida la entrada impar.
if numero % 2 == 0:
    print ("Ha ingresado un número par.")
else:
    print ("Por favor, ingrese un número par.")
    