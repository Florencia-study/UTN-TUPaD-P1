corte = 0
sumatoria = 0
print ("Ingrese un numero entero. Ingrese", corte, "para finalizar el proceso: ")
num = int (input())


while num != 0: 
    sumatoria += num
    print ("Ingrese un numero entero. Ingrese", corte, "para finalizar el proceso: ")
    num = int (input())

if num == corte: 
    print ("La suma de los numeros enteros ingresados es: ", sumatoria)