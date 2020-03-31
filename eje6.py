opcionesValidas = set(['+','-','*','/'])
opcionesTexto = "seleccione una de las siguientes opciones para trabajar con los numero: \n\r +: sumar números\n\r -: restar números\n\r *: multiplicar numeros\n\r /: dividir numeros\n\r"

"""FUNCIONES"""
"""
    Modulo para recibir numeros desde la entrada
"""
def procesarEntradaNumero():
    print("Ingrese un numero")
    texto = input()
    while (texto.isdecimal() == False):
        print("ingrese un numero decimal")
        texto = input()
    return int(texto)
"""
    Modulo para recibir el operador desde la entrada
"""
def procesarEntradaOperador():
    print("Ingrese un operador")
    texto = input()
    while ( texto not in opcionesValidas):
        print("ingrese un operador valido: + - * / ")
        texto = input()
    return texto


"""MAIN"""
numero1=procesarEntradaNumero()
numero2=procesarEntradaNumero()
print(opcionesTexto)
operador=procesarEntradaOperador()

if operador == "+":
    print("usted eligió suma")
    print(f"el resultado de {numero1}{operador}{numero2} es: {numero1 + numero2}")
elif operador == "-":
    print("usted eligió resta")
    print(f"el resultado de {numero1}{operador}{numero2} es: {numero1 - numero2}")
elif operador == "*":
    print("usted eligió producto")
    print(f"el resultado de {numero1}{operador}{numero2} es: {numero1 * numero2}")
elif operador == "/":
    print("usted eligió division")
    if numero2 != 0:
        print(f"el resultado de {numero1}{operador}{numero2} es: {numero1 / numero2}")
    else:
        print("no puede realizarse la division por cero MATH ERROR")
else:
    print("no es valido")

print("Fin de las operaciones")
