#programa para validar contrasenia.

contrasenia = input ("Ingrese su contrasenia: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
     