#7)Calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero_usuario=int(input("Ingrese un número entero positivo."))
suma=0
for i in range (0,numero_usuario+1):
    suma=i+suma
print(f"La suma de los números comprendidos entre el 0 y {numero_usuario} es {suma}. ")