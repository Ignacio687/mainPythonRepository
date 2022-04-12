from itertools import count

def buscarRepetidos(list):
    diccionarioRepetidos = {}
    for value in list:
        if value not in diccionarioRepetidos:
            diccionarioRepetidos[value] = list.count(value)
    return diccionarioRepetidos
    