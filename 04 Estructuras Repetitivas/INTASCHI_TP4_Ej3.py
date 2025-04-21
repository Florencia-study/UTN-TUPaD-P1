#3) sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 


print ("Ingrese un numero entero inicial.")
valor_incial = int(input())
print ("Ingrese un numero entero final.")
valor_final = int(input())
sumatoria = 0

for x in range (valor_incial+1,valor_final):
    sumatoria += x

print ("La suma de todos los numeros comprendidos entre los dos valores ingresados, excluyendo ambos extremos es, ", sumatoria)