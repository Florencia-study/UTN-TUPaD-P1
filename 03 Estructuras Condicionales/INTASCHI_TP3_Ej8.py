#ej 8. Opciones de escritura de nombre.

nombre = input ("Ingrese su nombre: ")
opcion = int (input ("Presione 1, si quiere su nombre en mayúsculas. Presione 2, si quiere su nombre en minusculas. Presione 3, si quiere la primera letra de su nombre en mayusculas."))

if opcion == 1:
    print (nombre.upper())
elif opcion == 2:
    print (nombre.lower())
elif opcion == 3:
    print (nombre.title())
else:
    print ("La opción ingresada no es válida.")

    