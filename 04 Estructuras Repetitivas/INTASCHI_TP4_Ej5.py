#5) el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#generar lista random entre 0 y 9. 

import random
lista = [0,1,2,3,4,5,6,7,8,9]
numero_incognito = random.choice(lista)
numero_adivinado = ("inf")
cont = 0


while numero_adivinado != numero_incognito:
    print ("Adivine el numero aleatorio entre 0 y 9 generado por el juego. Ingrese un numero entero.")
    numero_adivinado = int (input())
    cont += 1

print ("Felicitaciones! Juego ganado. El numero adivinaod es ", numero_adivinado, "y el numero incognito era ", numero_incognito)
print ("Numero de intentos: ", cont)








