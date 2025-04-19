#Programa notas.
nota = float (input ("Ingrese su nota:"))

#Si la nota es mayor o igual a 6, mostrar por pantalla un mensaje que diga “Aprobado”
if nota >= 6 and nota <= 10:
    print ("Aprobado")
elif nota < 6 and nota >= 0:
    print ("Desaprobado")
else:
    print ("La nota ingresada no es válida")
    