"""
Generar un menú que te permita realizar las siguientes opciones:

Menú de opciones para la lista de números a ingresar:
1: ingresar números
2: ordenar números
3: calcular el máximo
4: calcular el mínimo
5: calcular el promedio
0: para terminar

Se debe repetir hasta que se ingrese la opción 0. Se debe permitir agregar números aún luego de
haber utilizado las demás operaciones utilizando la opción 1. En caso que no se haya ingresado
ningún número indicar que la lista está vacía. Investigue las funciones max, min y sum.
"""

opcionesValidas = set([0,1,2,3,4,5])
opcionesTexto = "seleccione una de las siguientes opciones para trabajar con listas: \n\r 1: ingresar números\n\r 2: ordenar números\n\r 3: calcular el máximo\n\r 4: calcular el mínimo\n\r 5: calcular el promedio\n\r 0: para terminar \n\n\r"
listaNumeros=[]

"""
    Validacion para realizar continuar realizando operaciones de lista
    Parametro: int
    Retorno: boolean
"""
def validarContinuacion(number):
    if number != 0:
        return True
    else:
        return False


"""
    Interfas para el usuario usuario
    Parametro: ninguno
    Retorno: int
"""
def interfaz():
    print(opcionesTexto)                        #texto en pantalla con las operaciones disponibles
    opcion = input()
    while (opcion.isdecimal() == False):        #mantiene un loop hasta que se introduzca un decimal
        print("ingrese un numero decimal")
        opcion = input()
    opcion = int(opcion)
    while(opcion not in opcionesValidas):        #devuelve true si la opcion seleccionada no pertenece a una opcion valida
        print("Ingrese una opcion valida")
        opcion = int(input())
    return opcion
"""
    Modulo para cargar la lista con numeros
    Parametro: ninguno
    Retorno: int
"""
def cargarLista(lista):
    cantAnt=0
    texto = input()
    while True:
        while(  texto.isdecimal() == False  ):
            print("ingrese un numero decimal")
            texto = input()
        #si el numero ingresado es el 0 se termina la operacion
        if int(texto) == 0:
            break
        # convertimos texto a tipo int y agregamos el numero a la lista
        lista.append(int(texto))
        cantAnt = cantAnt + 1
        texto = input()

    if noEstaVacia(lista):
        print(f"elementos agregados en la lista: {cantAnt} ")
        print("Los elementos de la lista son los siguientes: ")
        print(lista)
        print("\n\n")
    return 0

"""
    Minifuncion para ver si la lista esta vacia o no
    Parametro: lista
    retorno: True o False
"""
def listaVacia(lista):
    return not lista            #si la lista esta vacia retorna True

"""
    Modulo para ver si la lista esta vacia
    Parametro: list
    Retorno: boolean
"""
def noEstaVacia(lista):
    if listaVacia(lista) == False:
        print(f"La lista tiene {len(lista)} elementos :) \n\n")
        return True
    else:
        print("La lista esta vacia T_T \n\n")
        return False

"""
    Modulo para ordenar la lista
    Parametro: list
    Retorno: int
"""
def ordenarLista(lista):
    print("Realizando operacion de ordenado...")
    lista.sort()
    print("operacion finalizada la lista ordenada es la siguiente: ")
    print(lista)
    print("\n\n")
    return 0

"""
    Modulo para el maximo de la lista
    Parametro: list
    Retorno: int
"""
def maxLista(lista):
    print("Realizando operacion de buscar el maximo...")
    print("operacion finalizada el maximo de la lista es el siguiente: ")
    print(max(lista))
    print("\n\n")
    return 0

"""
    Modulo para el minimo de la lista
    Parametro: list
    Retorno: int
"""
def minLista(lista):
    print("Realizando operacion de buscar el minimo...")
    print("operacion finalizada el minimo de la lista es el siguiente: ")
    print(min(lista))
    print("\n\n")
    return 0

"""
    Modulo para el promedio de la lista
    Parametro: list
    Retorno: int
"""
def promLista(lista):
    print("Realizando operacion de calcular el promedio...")
    print("operacion finalizada el promedio es el siguiente: ")
    print(sum(lista)/len(lista))
    print("\n\n")
    return 0


"""main"""
#llamada al modulo interfaz
opcion = interfaz()
#verificar si continua o no realizando operaciones de lista
continuar = validarContinuacion(opcion)


#comienza el bucle de operaciones
while(continuar):
    if opcion == 1:
        print("ingrese numeros para terminar la operacion de ingresar numero ingrese 0")
        cargarLista(listaNumeros)
    elif opcion == 2:
        print("usted eligió ordenar")
        if noEstaVacia(listaNumeros):
            ordenarLista(listaNumeros)
    elif opcion == 3:
        print("usted eligió maximo")
        if noEstaVacia(listaNumeros):
            maxLista(listaNumeros)
    elif opcion == 4:
        print("usted eligió minimo")
        if noEstaVacia(listaNumeros):
            minLista(listaNumeros)
    elif opcion == 5:
        print("usted eligió promedio")
        if noEstaVacia(listaNumeros):
            promLista(listaNumeros)
    else:
        print("Terminar operacion de listas esta seguro Y/N")
        confirmacion = input()
        if confirmacion.lower() == "y":
            continuar = False
    if continuar == True:
        opcion = interfaz()
print("Fin de las operaciones con lista de numeros")



