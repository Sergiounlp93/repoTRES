import re
from builtins import int

def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #de lo contrario devuelve Verdadero

"""
    modulo que sirve para contar caracteres
    parametro: char[] , char
    retorno: int
"""
def contarCaracter(frase, letra):
    cuenta = 0
    for caracter in frase:
        if caracter == letra:
            cuenta += 1
    return cuenta

"""
    modulo que sirve para descomponer e informar por cada caracter la cantidad de ocurrencias correspondiente 
    parametro: char[] , char
    retorno: int
"""
def interfaz(cadena):
    conjunto = set(cadena)  #usamos conjuntos para no tener caracteres repetidos y haci poder iterar por caracter una unica vez
    for letra in conjunto:
        cantidad = contarCaracter(cadena,letra)
        print(f"{letra} es :{cantidad}")
        if es_primo(cantidad):
            print("es primo")
    return 0


"""MAIN"""
frase = input("introduzca una frase: ")
interfaz(frase)