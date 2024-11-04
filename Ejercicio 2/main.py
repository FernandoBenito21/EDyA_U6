from Dirigido_Sec import *
import numpy as np
import random

if __name__ == '__main__':
    cant_nodos = 4
    grafo1 = Grafo_Dirigido_Sec(cant_nodos)
    op = 1
    while(op != 0):
        print(f"Inserta un par de nodos del 0 al {cant_nodos - 1}")
        u = int(input('primer nodo: '))
        v = int(input('segundo nodo: '))
        grafo1.Insertar(u, v)
        op = int(input('Continuar? 1 si, 0 no: '))
    grafo1.Mostrar()
    conexo = grafo1.Conexo()
    if (conexo == True):
        print("El grafo es conexo")
    else:
        print("El grafo no es conexo")
    aciclico = grafo1.Aciclico()
    if (aciclico == True):
        print("El grafo es aciclico")
    else:
        print("El grafo no es aciclico")