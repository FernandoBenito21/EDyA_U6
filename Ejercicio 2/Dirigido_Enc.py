import numpy as np
from Cola import Cola_Encadenada
from Pila import Pila_Encadenada
from Nodos import Nodo

class Dirigido_Encadenado:
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
            aux.setSig(Nodo(v))
        
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
    
    def BEP_C(self, u, visitados):
        visitados[u] = True
        for v in self.Adyacentes(u):
            if (visitados[v] == False):
                self.BEP_C(v, visitados)
    
    def Aciclico(self):
        visitado = np.full(self.__cant, False, dtype=bool)
        pila = np.full(self.__cant, False, dtype=bool)
        for i in range(self.__cant):
            if (visitado[i] == False):
                if (self.Aciclico_P(i, visitado, pila) == True):
                    return False
        return True

    def Aciclico_P(self, v, visitado, pila):
        visitado[v] = True
        pila[v] = True
        for u in self.Adyacentes(v):
            if (visitado[u] == False):
                if (self.Aciclico_P(u, visitado, pila) == True):
                    return True
            else:
                if (pila[u] == True):
                    return True
        pila[v] = False
        return False
    
    def Conexo(self):
        visitados = np.full(self.__cant, False, dtype = bool)
        self.BEP_C(0, visitados)
        if (all(visitados) == False):
            return False
        else:
            fuerte = True
            i = 1
            while (i < self.__cant) and (fuerte == True):
                visitados = np.full(self.__cant, False, dtype = bool)
                self.BEP_C(i, visitados)
                if (all(visitados) == False):
                    fuerte = False
                i += 1
            if (fuerte == True):
                print("El grafo es fuertemente conexo")
            else:
                print("El grafo es simple conexo")
            return True
        '''para BEP_2:
        visitados = self.BEP_2(0)
        if (len(visitados) == self.__cant):
            fuerte = True
            i = 1
            while (i < self.__cant) and (fuerte == True):
                visitados = self.BEP_2(i)
                if (len(visitados) < self.__cant):
                    fuerte = False
                i += 1
            if (fuerte == True):
                print("El grafo es fuertemente conexo")
            else:
                print("El grafo es simple conexo")
            return True
        else:
            return False'''
    
    def GradEnt(self, u):
        grado = 0
        for i in range(self.__cant):
            aux = self.__lista[i]
            while (aux != None)(aux.getItem() != u):
                aux = aux.getSig()
            if (aux != None):
                grado += 1
        print(f"El grado de entrada del nodo {u} es {grado}")
    
    def GradSal(self, u):
        grado = 0
        aux = self.__lista[u]
        while (aux != None):
            grado += 1
            aux = aux.getSig()
        print(f"El grado de salida de {u} es de {grado}")
    
    def NodoF(self, u):
        if (self.__lista[u] != None):
            i = 0
            salida = False
            while (i < self.__cant) and (salida == False):
                aux = self.__lista[i]
                while (aux != None) and (aux.getItem() != u):
                    aux = aux.getSig()
                if (aux != None):
                    salida = True
            if (salida == True):
                return False
            else:
                return True
        else:
            return False
    
    def NodoS(self, u):
        if (self.__lista[u] == None):
            i = 0
            salida = False
            while (i < self.__cant) and (salida == False):
                aux = self.__lista[i]
                while (aux != None) and (aux.getItem() != u):
                    aux = aux.getSig()
                if (aux != None):
                    salida = True
            if (salida == True):
                return True
            else:
                return False
        else:
            return False
    
    def Ordenacion_Topologica(self, v, marca):
        marca[v] = True
        for w in self.Adyacentes(v):
            if (marca[w] == False):
                self.Ordenacion_Topologica(w, marca)
        print(f"{v}")
    
    