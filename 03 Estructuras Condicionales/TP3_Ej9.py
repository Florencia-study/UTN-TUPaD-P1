#ej 9

magnitud = float (input ("Ingrese la magnitud del terremoto:"))

#Estructura condicional para clasificar la magnitud, segun la escala de Richter.

if magnitud <3:
    print ("Categoria: Muy leve - Imperceptible.")
elif magnitud >= 3 and magnitud < 4:
    print ("Categoria: Leve - ligeramente perceptible.")
elif magnitud >= 4 and magnitud < 5:
    print ("Categoria: Moderado - sentido por personas, pero generalmente no causa daños.")
elif magnitud >= 5 and magnitud < 6:
    print ("Categoria: Fuerte - puede causar daños en estructuras débiles.")
elif magnitud >= 6 and magnitud < 7:
    print ("Categoria: Muy fuerte - puede causar daños significativos.")
else:
    print ("Categoria: Extremo - puede causar graves daños a gran escala")