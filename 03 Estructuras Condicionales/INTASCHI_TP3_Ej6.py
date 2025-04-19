#ej 6. paquete statistics
from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


mean(numeros_aleatorios) 
mode(numeros_aleatorios)
median(numeros_aleatorios)



#moda (mode), la mediana (median) y la media (mean) 

print ("media: ", mean (numeros_aleatorios))
print ("moda: ", mode (numeros_aleatorios))
print ("mediana: ", median (numeros_aleatorios))

if mean (numeros_aleatorios) > median (numeros_aleatorios) and median (numeros_aleatorios) > mode (numeros_aleatorios):
    print ("El sesgo es positivo o a la derecha")
elif mean (numeros_aleatorios) < median (numeros_aleatorios) and median (numeros_aleatorios) < mode (numeros_aleatorios):
    print ("El sesgo es negativo o a la izquierda. ")
elif mean (numeros_aleatorios) == median (numeros_aleatorios) and median (numeros_aleatorios) == mode (numeros_aleatorios):
    print ("No hay sesgo. ")
else:
    print ("No se puede determinar el sesgo. ")