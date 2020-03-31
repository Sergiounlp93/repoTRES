""" Version extendida """
"""
#Creamos 2 variables usando asignación múltiple nos servirá para indicarle al usuario si la palabra ingresada es o no es palíndromo
igual, aux = 0, 0
#Solicitamos al usuario que ingrese una palabra y leemos dicha palabra usando la función input() para procesarla mas adelante
texto = input("Ingrese la palabra que desea evaluar: ")
for ind in reversed(range(0, len(texto))): #el bucle for va a iterar sobre un rango de números, pero sera un rango invertido
  if texto[ind].lower() == texto[aux].lower(): # la variable local ind y será usada para iterar de forma invertida sobre el string
    igual += 1
  aux += 1
if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")
"""


"""Version corta"""
"""
texto = input("Ingrese una palabra: ")
rever = texto[::-1]
if texto == rever:
    print("La palabra ingresada si es palindromo!!")
else:
    print("La palabra ingresada no es palindromo!!")
"""