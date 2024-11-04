import numpy as np
from Cola import Cola_Encadenada
from Pila import Pila_Encadenada
from Nodos import Nodo

class Grafo_Encadenado:
    __cant : int
    __lista : object
    
    def __init__(self, cant):
        self.__cant = cant
        self.__lista = np.full(cant, None, dtype = object)
    
    def Insertar(self, u, v):
        if (self.__lista[u] == None):
            self.__lista[u] = Nodo(v)
        else:
            aux = self.__lista[u]
            while (aux.getSig() != None):
                aux = aux.getSig()
        if (self.__lista[v] == None):
            self.__lista[v] = Nodo(u)
        else:
            aux.setSig(Nodo(v))
            aux = self.__lista[v]
            while (aux.getSig() != None):
                aux = aux.getSig()
            aux.setSig(Nodo(u))
    
    def Mostrar(self):
        print("Lista de adyacencia: ")
        for i in range(self.__cant):
            print(f"Nodo {i}: ")
            aux =self.__lista[i]
            while (aux != None):
                print(f"{aux.getItem()}")
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
            aux = self.__lista[u]
            while (aux.getItem() != v):
                print(f"{aux.getItem()}")
                aux = aux.getSig()
            print(f"{aux.getItem()}")
            
    def BEA(self, s):
        d = np.empty(self.__cant, dtype = int)
        cola = Cola_Encadenada()
        for i in range(self.__cant):
            d[i] = -1
        d[s] = 0
        cola.Insertar(s)
        while (cola.Vacia() == False):
            v = cola.Suprimir()
            for adyacente in self.Adyacentes(v):
                u = adyacente.getDato()
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
                for adyacente in self.Adyacentes(v):
                    u = adyacente.getDato()
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
        for adyacente in self.Adyacentes(s):
            u = adyacente.getDato()
            if (d[u] == 0):
                self.BEP_Visita(u, d, f, tiempo)
        tiempo[0] += 1
        f[s] = tiempo[0]
        
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
            for adyacente in adyacentes:
                i = adyacente.getDato()
                if (visitado[i] == False):
                    visitado[i] = True
                    cola.Insertar(i)
                    cont_visitados += 1
        if (cont_visitados == self.__cant):
            return True
        else:
            return False