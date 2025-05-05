#ej 9

contador=1  #para indicar la cantidad de veces que el usuario puede ingresar un numero (hasta 100.)
suma=0
corte="*"
entrada_usuario=""



while contador <=100 and entrada_usuario!=corte:
    entrada_usuario=(input(f"Ingrese un numero entero. Ingrese {corte} para finalizar."))
    if entrada_usuario!=corte:
        numero_usuario=int(entrada_usuario)
        contador+=1
        suma+=numero_usuario
    elif entrada_usuario==corte:
        media=suma/(contador-1)
        print (f"La media de la suma de los numeros ingresados es {media}.")
   

media=suma/(contador-1)

if entrada_usuario!=corte: 
    print(f"La media de la suma de los numeros ingresados es {media}.")