from Dirigido_Sec import *
import numpy as np

def Conversor(char):
        if (char == 'A-E II'):
            u = 0
        elif (char == 'A-E III'):
            u = 1
        elif (char == 'ED I'):
            u = 2
        elif (char == 'ED II'):
            u = 3
        elif (char == 'ED III'):
            u =  4
        elif (char == 'Trad-Int'):
            u = 5
        return u

if __name__=='__main__':
    grafo = Grafo_Dirigido_Sec(6)
    op = 1
    while (op != 0):
        print("Opciones: ")
        print("1.Cargar Grafo")
        print("2.Mostrar Orden Topologico")
        print("3.Ver matriz")
        print("0.Salir")
        op = int(input('Ingrese una opcion: '))
        if (op == 1):
            continuar = 1
            while (continuar != 0):
                u = int(input('Ingrese nodo origen: '))
                v = int(input('Ingrese nodo destino: '))
                grafo.Insertar(u, v)
                continuar = int(input('Continuar? 0 para no, cualquier otro para si: '))
        elif (op == 2):
            marca = np.full(6, False, dtype = bool)
            materia = input('Ingrese la materia inicial: ')
            v = Conversor(materia)
            print("Al derecho: ")
            grafo.Procesa_OT(v)
            print("Al revés: ")
            grafo.Ordenacion_Topologica(v, marca)
        elif (op == 3):
            grafo.Mostrar()                                                                                                                                                                                                                                                              