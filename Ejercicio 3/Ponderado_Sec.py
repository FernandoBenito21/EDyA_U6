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
    
    def Adyacentes(self, u):
        adyacentes = []
        for j in range(self.__cant):
            if (self.__matriz[u, j] != 0):
                adyacentes.append(j)
        return adyacentes
    
    def Camino(self, u, v):
        d = self.BEA(u)
        if (d[v] == -1):
            print(f"El nodo {v} no es alcanzable desde el nodo {u}.")
        else:
            camino = Pila_Encadenada()
            actual = v
            while (actual != u):
                camino.Insertar(actual)
                predecesor = 0
                encontrado = False
                while (predecesor < self.__cant) and (encontrado == False):
                    if (self.__matriz[predecesor, actual] != 0):
                        actual = predecesor
                        encontrado = True
                    predecesor += 1
            camino.Insertar(u)
            print(f"El camino desde {u} a {v} es: ")
            while (camino.Vacia() == False):
                print(f"{camino.Suprimir()}")
    
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
            if (vertice == 0):
                print("Ana")
            elif (vertice == 1):
                print("Belén")
            elif (vertice == 2):
                print("Cecilia")
            elif (vertice == 3):
                print("Daniel")
            elif (vertice == 4):
                print("Ezequiel")
            elif (vertice == 5):
                print("Federico")
        print(f"El costo minimo del envio es de: {T[v].getDistancia()}")
        
    def Camino_Minimo(self):
        Q = self.__matriz.copy()
        for k in range(self.__cant):
            for i in range(self.__cant):
                for j in range(self.__cant):
                    Q[i, j] = min(Q[i, j], (Q[i, k] + Q[k, j]))
        return Q