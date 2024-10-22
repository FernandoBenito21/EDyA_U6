import numpy as np
from Cola import Cola_Encadenada
from Pila import Pila_Encadenada

class Grafo:
    def __init__(self, n):
        self.__cant = n
        self.__matriz = np.full((n, n), 0, dtype = int)
    
    def Insertar(self, u, v):
        if (u < self.__cant) and (v < self.__cant):
            if (self.__matriz [u, v] == 1):
                print("Ya se insertó una arista entre estos nodos")
            else:
                self.__matriz[u, v] = 1
                self.__matriz[v, u] = 1
        else:
            print(f"Los nodos deben ser de un valor entre 0 y {self.__cant - 1}")
    
    def Mostrar(self):
        for i in range(self.__cant):
            print(' '.join(map(str, self.__matriz[i])))
    
    def Adyacentes(self, u):
        adyacentes = []
        for j in range(self.__cant):
            if (self.__matriz[u, j] == 1):
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
                    if (self.__matriz[predecesor, actual] == 1):
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
    
    def Warshall(self):
        P = self.__matriz.copy()
        for k in range(self.__cant):
            for i in range(self.__cant):
                for j in range(self.__cant):
                    P = P[i, j] or (P[i, k] and P[k, j])
        return P
        
    def Aciclico(self):
        visitado = np.full(self.__cant, False, dtype=bool)
        for i in range(self.__cant):
            if (visitado[i] == False):
                if (self.Aciclico_P(i, visitado, -1) == True):
                    return False
        return True

    def Aciclico_P(self, v, visitado, anterior):
        visitado[v] = True
        for u in self.Adyacentes(v):
            if (visitado[u] == False):
                if (self.Aciclico_P(u, visitado, v) == True):
                    return True
            else:
                if (u != anterior):
                    return True
        return False
    
    def Conexo(self):
        visitado = np.full(self.__cant, False, dtype = bool)
        cola = Cola_Encadenada()
        cola.Insertar(0)
        visitado[0] = True
        cont_visitados = 1
        while (cola.Vacia() == False):
            actual = cola.Suprimir()
            adyacentes = self.Adyacentes(actual)
            for i in adyacentes:
                if (visitado[i] == False):
                    visitado[i] = True
                    cola.Insertar(i)
                    cont_visitados += 1
        if (cont_visitados == self.__cant):
            return True
        else:
            return False
    
    
    