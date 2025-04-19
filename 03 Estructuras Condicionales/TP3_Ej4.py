#Programa que indica la categoría etaria a la que pertenece el usuario. 

edad = int (input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
    print ("Pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print ("Pertenece a la categoria Adolescente")
elif edad >= 18 and edad < 30:
    print ("Pertenece a la categoria Adulto/a joven")	
elif edad >= 30: 
    print ("Pertenece a la categoria Adulto/a")
else :
    print ("El valor ingresado es incorrecto.")