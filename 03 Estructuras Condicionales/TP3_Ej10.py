#ej 10. Estaciones segun el hemisferio.

hemisferio = input ("Ingrese el hemisferio (N/S): ").upper()
mes = (input ("Ingrese el mes: ")).title()
dia = int (input ("Ingrese el dia: "))

#evaluacion de la estacion segun el hemisferio.

if hemisferio == "N":
    if (mes == "Diciembre"and dia >= 21 and dia <= 31) or (mes == "Enero"and dia >= 1 and dia <= 31) or (mes == "Febrero"and dia >=1 and dia <= 28) or (mes == "Marzo"and dia >= 1 and dia <= 20):
        print ("Se encuentra en invierno.")
    elif (mes == "Marzo"and dia >= 21 and dia <= 31) or (mes == "Abril"and dia >= 1 and dia <= 30) or (mes == "Mayo"and dia >=1 and dia <= 31) or (mes == "Junio"and dia >= 1 and dia <= 20):
        print ("Se encuentra en primavera.")
    elif (mes == "Junio"and dia >= 21 and dia <= 30) or (mes == "Julio"and dia >= 1 and dia <= 31) or (mes == "Agosto"and dia >=1 and dia <= 31) or (mes == "Septiembre"and dia >= 1 and dia <= 20):
        print ("Se encuentra en verano.")
    elif (mes == "Septiembre"and dia >= 21 and dia <= 30) or (mes == "Octubre"and dia >= 1 and dia <= 31) or (mes == "Noviembre"and dia >=1 and dia <= 30) or (mes == "Diciembre"and dia >= 1 and dia <= 20):
        print ("Se encuentra en otonio.")
    else:
        print ("El mes o dia ingresado no es válido.")
elif hemisferio == "S": 
   if (mes == "Diciembre"and dia >= 21 and dia <= 31) or (mes == "Enero"and dia >= 1 and dia <= 31) or (mes == "Febrero"and dia >=1 and dia <= 28) or (mes == "Marzo"and dia >= 1 and dia <= 20):
        print ("Se encuentra en verano.")
   elif (mes == "Marzo"and dia >= 21 and dia <= 31) or (mes == "Abril"and dia >= 1 and dia <= 30) or (mes == "Mayo"and dia >=1 and dia <= 31) or (mes == "Junio"and dia >= 1 and dia <= 20):
        print ("Se encuentra en otonio.")
   elif (mes == "Junio"and dia >= 21 and dia <= 30) or (mes == "Julio"and dia >= 1 and dia <= 31) or (mes == "Agosto"and dia >=1 and dia <= 31) or (mes == "Septiembre"and dia >= 1 and dia <= 20):
        print ("Se encuentra en invierno.")
   elif (mes == "Septiembre"and dia >= 21 and dia <= 30) or (mes == "Octubre"and dia >= 1 and dia <= 31) or (mes == "Noviembre"and dia >=1 and dia <= 30) or (mes == "Diciembre"and dia >= 1 and dia <= 20):
        print ("Se encuentra en primavera.") 
   else:
        print ("El mes o dia ingresado no es válido.")
else:
    print ("Alguno de los valores  ingresados no es válido.")

