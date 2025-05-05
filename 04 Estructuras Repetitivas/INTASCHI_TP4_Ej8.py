contador=1  #para indicar la cantidad de veces que el usuario puede ingresar un numero (hasta 100.)
cant_pares=0
cant_impares=0
cant_negativos=0
cant_positivos=0

while contador <=100:
    numero_usuario=int(input("Ingrese un numero entero."))
    contador+=1
    #eval.pares/impares
    if numero_usuario%2==0:
        cant_pares+=1
    else:
        cant_impares+=1
    if numero_usuario>=0:
        cant_positivos+=1
    else:
        cant_negativos+=1
    

print(f"Usted ingreso {cant_pares} numeros pares, {cant_impares} numeros impares, {cant_positivos} numeros positivos, y {cant_negativos} numeros negativos.")
