from Grafo_Sec import *

if __name__ == '__main__':
    cant_nodos = 5
    grafo1 = Grafo(cant_nodos)
    op = 1
    while(op != 0):
        print("Inserta un par de nodos del 0 al {cant_nodos - 1}")
        u = int(input('primer nodo: '))
        v = int(input('segundo nodo: '))
        grafo1.Insertar(u, v)
        op = int(input('Continuar? 1 si, 0 no: '))
    grafo1.Adyacentes(0)
    grafo1.Camino(0, 3)
    grafo1.Camino(0, 4)
    grafo1.Mostrar()