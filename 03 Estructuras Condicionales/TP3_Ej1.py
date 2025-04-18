#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print ("Es mayor de edad")

    #No lo pide la actividad, pero se podria añadir al código un elif para aclarar si su edad está entre 0 y 18, que diga que es menor de edad, y si la edad ingresada es menor que cero, indicar que el valor ingresado es incorrecto.