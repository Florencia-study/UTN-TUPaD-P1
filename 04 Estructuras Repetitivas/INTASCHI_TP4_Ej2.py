#2) solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

num = int(input("Ingrese un número entero: "))
cont = 0

num = (abs(num))
while num > 0:
   #divido mi numero por 10 y que quede solo la parte entera , de esta forma me aseguro que el numero vaya perdiendo un digito
   num = num//10 
   #al dividir por 10 y por lo tanto perder un digito, mi contador sube en 1. Esa es la cant de digitos que va a tener mi numero.
   cont += 1 

print ("El numero ingresado tiene ", cont, "digitos.")
   
