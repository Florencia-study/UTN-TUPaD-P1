#ejercicio 7. String terminado en vocal.

frase = input ("Ingrese una frase: ")
if frase[-1] == "a" or frase[-1] == "e" or frase[-1] == "i" or frase[-1] == "o" or frase[-1] == "u":
    print (f"{frase}!")
else:
    print (frase)