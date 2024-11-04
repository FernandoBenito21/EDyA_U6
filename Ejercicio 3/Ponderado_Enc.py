import numpy as np
from Cola import Cola_Encadenada
from Pila import Pila_Encadenada
from Nodos import Reg_Dijkstra, Vertice_Ponderado

class Ponderado_Encadenado:
    def __init__(self, cant):
        self.__cant = cant
        self.__lista = np.full(cant, None, dtype = object)
    
    def Insertar(self, u, v, p):
        if (self.__lista[u] == None):
            self.__lista[u] = Vertice_Ponderado(v, p)
        else:
            aux = self.__lista[u]
            while (aux.getSig() != None):
                aux = aux.getSig()
            aux.setSig(Vertice_Ponderado(v, p))
    
    def Mostrar(self):
        print("Lista de adyacencia: ")
        for i in range(self.__cant):
            n1 = self.Convertir(i)
            aux = self.__lista[i]
            while (aux != None):
                n2 = self.Convertir(aux.getDato())
                print(f"{n1} -{aux.getPeso()} -> {n2}")
                aux = aux.getSig()
    
    def Adyacentes(self, u):
        adyacentes = []
        aux = self.__lista[u]
        while (aux != None):
            adyacentes.append(aux)
            aux = aux.getSig()
        return adyacentes
    
    def Dijkstra(self, inicial):
        T = [Reg_Dijkstra() for _ in range(self.__cant)]
        T[inicial].setDistancia(0)    
        v = 0
        for i in range(self.__cant):
            min_dist = float('inf')
            for j in range(self.__cant):
                if (T[j].getConocido() == False) and (T[j].getDistancia() < min_dist):
                    min_dist = T[j].getDistancia()
                    v = j
            T[v].setConocido(True)
            for w in self.Adyacentes(v):
                if (T[w.getDato()].getConocido() == False):
                    if ((T[v].getDistancia() + w.getPeso()) < T[w.getDato()].getDistancia()):
                        T[w.getDato()].setDistancia(T[v].getDistancia() + w.getPeso())
                        T[w.getDato()].setCamino(v)    
        return T
    
    def Procesa_Dijkstra(self, u, v):
        T = self.Dijkstra(u)
        camino = Pila_Encadenada()
        c = v
        while (c != u):
            camino.Insertar(c)
            c = T[c].getCamino()
        camino.Insertar(u)
        n1 = self.Convertir(u)
        n2 = self.Convertir(v)
        print(f"El camino minimo para enviar un SMS de {n1} para {n2} es:")
        while (camino.Vacia() == False):
            vertice = camino.Suprimir()
            nombre = self.Convertir(vertice)
            print(nombre)
        print(f"El costo minimo del envio es de: {T[v].getDistancia()}")
    
    def Convertir(self, vertice):
        if (vertice == 0):
            char = 'Ana'
        elif (vertice == 1):
            char = "Belén"
        elif (vertice == 2):
            char = "Cecilia"
        elif (vertice == 3):
            char = "Daniel"
        elif (vertice == 4):
            char = "Ezequiel"
        elif (vertice == 5):
            char = "Federico"
        return char