import numpy as np
from Cola import Cola_Encadenada
from Pila import Pila_Encadenada

class Grafo_Dirigido_Sec:
    def __init__(self, cant):
        self.__cant = cant
        self.__matriz = np.full((cant, cant), 0, dtype = int)
    
    def Insertar(self, u, v):
        if (u < self.__cant) and (v < self.__cant):
            self.__matriz[u, v] = 1
        else:
            print(f"Los nodos deben tener un valor entre 0 y {self.__cant - 1}")
    
    def Mostrar(self):
        for i in range(self.__cant):
            print(' '.join(map(str, self.__matriz[i])))
    
    def Mostrar_2(self):
        for i in range(self.__cant):
            char = self.Conversor(i)
            for j in self.Adyacentes(i):
                char2 = self.Conversor(j)
                print(f"{char} -> {char2}")
    
    def Adyacentes(self, u):
        adyacentes = []
        for j in range(self.__cant):
            if (self.__matriz[u, j] == 1):
                adyacentes.append(j)
        return adyacentes
    
    def BEP_2(self, s): #ordenacion topologica?
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
    
    def Ordenacion_Topologica(self, v, marca):
        marca[v] = True
        for w in self.Adyacentes(v):
            if (marca[w] == False):
                self.Ordenacion_Topologica(w, marca)
        c = self.Conversor(v)
        print(c)
    
    def Procesa_OT(self, u):
        lista = self.BEP_2(u)
        for nodo in lista:
            char = self.Conversor(nodo)
            print(char)
    
    def Conversor(self, u):
        if (u == 0):
            char = 'A-E II'
        elif (u == 1):
            char = 'A-E III'
        elif (u == 2):
            char = 'ED I'
        elif (u == 3):
            char = 'ED II'
        elif (u == 4):
            char = 'ED III'
        elif (u == 5):
            char = 'Trad-Int'
        return char