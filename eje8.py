import re
from builtins import int

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
    return 0


"""MAIN"""
frase = input("introduzca una frase: ")
interfaz(frase)