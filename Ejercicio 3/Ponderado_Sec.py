import numpy as np
from Cola import Cola_Encadenada
from Pila import Pila_Encadenada
from Nodos import Reg_Dijkstra

class Grafo_Ponderado_Sec:
    def __init__(self, cant):
        self.__cant = cant
        self.__matriz = np.full((cant, cant), 0, dtype = int)
    
    def Insertar(self, u, v, p):
        if (u < self.__cant) and (v < self.__cant):
            self.__matriz[u, v] = p
        else:
            print(f"Los nodos deben tener un valor entre 0 y {self.__cant - 1}")
    
    def Mostrar(self):
        for i in range(self.__cant):
            print(' '.join(map(str, self.__matriz[i])))
            
    def Mostrar_2(self):
        for i in range(self.__cant):
            n1 = self.Conversor(i)
            for j in self.Adyacentes(i):
                n2 = self.Conversor(j)
                print(f"{n1} -{self.__matriz[i, j]}-> {n2}")
            
    def Adyacentes(self, u):
        adyacentes = []
        for j in range(self.__cant):
            if (self.__matriz[u, j] != 0):
                adyacentes.append(j)
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
                if (T[w].getConocido() == False):
                    if ((T[v].getDistancia() + self.__matriz[v, w]) < T[w].getDistancia()):
                        T[w].setDistancia(T[v].getDistancia() + self.__matriz[v, w])
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
        print(f"El camino minimo para enviar un SMS de {u} para {v} es:")
        while (camino.Vacia() == False):
            vertice = camino.Suprimir()
            nombre = self.Conversor(vertice)
            print(nombre)
        print(f"El costo minimo del envio es de: {T[v].getDistancia()}")
        
    def Conversor(self, u):
        if (u == 0):
            char = 'Ana'
        elif (u == 1):
            char = 'Belén'
        elif (u == 2):
            char = 'Cecilia'
        elif (u == 3):
            char = 'Daniel'
        elif (u == 4):
            char = 'Ezequiel'
        elif (u == 5):
            char = 'Federico'
        return char