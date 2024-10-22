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
            print(f"Nodo {i}: ")
            aux =self.__lista[i]
            while (aux != None):
                print(f"{aux.getDato()}")
                aux = aux.getSig()
    
    def Adyacentes(self, u):
        adyacentes = []
        aux = self.__lista[u]
        while (aux != None):
            adyacentes.append(aux)
            aux = aux.getSig()
        return adyacentes
    
    def Camino(self, u, v):
        d = self.BEA(u)
        if (d[v] == -1):
            print(f"El nodo {v} no es alcanzable desde el nodo {u}.")
        else:
            print(f"El camino de {u} a {v}")
            peso = 0
            aux = self.__lista[u]
            while (aux.getItem() != v):
                print(f"{aux.getItem()}")
                peso += aux.getPeso()
                aux = aux.getSig()
            print(f"{aux.getItem()}")
            peso += aux.getPeso()
            print(f"Peso total: {peso}")
    
    def BEA(self, s):
        d = np.empty(self.__cant, dtype = int)
        cola = Cola_Encadenada()
        for i in range(self.__cant):
            d[i] = -1
        d[s] = 0
        cola.Insertar(s)
        while (cola.Vacia() == False):
            v = cola.Suprimir()
            for u in self.Adyacentes(v):
                if (d[u] == -1):
                    d[u] = d[v] + 1
                    cola.Insertar(u)
        return d 
    
    def BEP(self, s):
        visitado = np.full(self.__cant, False, dtype=bool)
        resultado = []
        pila = Pila_Encadenada() 
        pila.Insertar(s)
        while (pila.Vacia() == False):  
            v = pila.Suprimir()  
            if (visitado[v] == False): 
                visitado[v] = True
                resultado.append(v)
                for u in self.Adyacentes(v):
                    if (visitado[u] == False):
                        pila.Insertar(u)
        return resultado
    
    def BEP_2(self):
        d = np.full(self.__cant, 0, dtype=int)  
        f = np.full(self.__cant, 0, dtype=int)
        tiempo = [0]
        for s in range(self.__cant):
            if d([s] == 0):
                self.BEP_Visita(s, d, f, tiempo)
        return d, f

    def BEP_Visita(self, s, d, f, tiempo):
        tiempo[0] += 1
        d[s] = tiempo[0]
        for u in self.Adyacentes(s):
            if (d[u] == 0):
                self.BEP_Visita(u, d, f, tiempo)
        tiempo[0] += 1
        f[s] = tiempo[0]
    
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
                if (T[w].getConocido() == False):
                    if ((T[v].getDistancia() + w.getPeso()) < T[w].getDistancia()):
                        T[w].setDistancia(T[v].getDistancia() + w.getPeso())
                        T[w].setCamino(v)    
        return T
    
    def Procesa_Dijkstra(self, u, v):
        T = self.Dijkstra(u)
        camino = Pila_Encadenada()
        c = v
        while (c != u):
            camino.Insertar(c)
            c = T[c].getCamino()
        camino.Insertar(u)
        print(f"El camino minimo desde {u} hasta {v} es:")
        while (camino.Vacia() == False):
            print(f"{camino.Suprimir()}")
        print(f"Y el peso del camino minimo es de {T[v].getDistancia()}")