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
                anterior = 0
                encontrado = False
                while (anterior < self.__cant) and (encontrado == False):
                    if (self.__matriz[anterior, actual] == 1):
                        actual = anterior
                        encontrado = True
                    anterior += 1
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
    
    def BEP(self):
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
    
    def BEP_C(self, u, visitados):
        visitados[u] = True
        for v in self.Adyacentes(u):
            if (visitados[v] == False):
                self.BEP_C(v, visitados)
    
    def Aciclico2(self):
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
    
    def Aciclico(self, v = 0, visitados = None, pila = None):
        if (visitados is None):
            visitados = np.full(self.__cant, False, dtype = bool)
            pila = np.full(self.__cant, False, dtype = bool)
            for i in range(self.__cant):
                if (visitados[i] == False):
                    if (self.Aciclico(v = 0, visitados = visitados, pila = pila) == True):
                        return False
            return True
        else:
            visitados[v] = True
            pila[v] = True
            for u in self.Adyacentes(v):
                if (visitados[u] == False):
                    if (self.Aciclico(v = u, visitados = visitados, pila = pila) == True):
                        return True
                else:
                    if(pila[u] == True):
                        return True
            pila[v] = False
            return False
    
    def Conexo3(self):
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
    
    def BEP_Conexo(self, nodo, visitados, matriz):
        visitados[nodo] = True
        for j in range(self.__cant):
            if[matriz[nodo, j] == 1] and [visitados[j] == False]:
                self.BEP_Conexo(j, visitados, matriz)
    
    def Conexo_2(self):
        visitados = np.full(self.__cant, False, dtype = bool)
        self.BEP_Conexo(0, visitados, self.__matriz)
        if (all(visitados) == True):
            visitados.fill(False)
            traspuesta = self.__matriz.transpose()
            self.BEP_Conexo(0, visitados, traspuesta)
            if (all(visitados) == True):
                print("El grafo es fuertemente conexo")
            else:
                print("El grafo es simple conexo")
            return True
        else:
            return False
    
    def Conexo(self, nodo = 0, visitados = None, matriz = None):
        if (matriz is None):
            matriz = self.__matriz
            visitados = np.full(self.__cant, False, dtype = bool)
            self.Conexo(nodo = 0, visitados = visitados, matriz = matriz)
            if (all(visitados) == True):
                visitados.fill(False)
                traspuesta = matriz.transpose()
                self.Conexo(nodo = 0, visitados = visitados, matriz = traspuesta)
                if(all(visitados) == True):
                    print("El grafo es fuertemente conexo")
                else:
                    print("El grafo es simple conexo")
                return True
            else:
                return False
        else:
            visitados[nodo] = True
            for j in range(self.__cant):
                if (matriz[nodo, j] != 0) and (visitados[j] == False):
                    self.Conexo(nodo = j, visitados = visitados, matriz = matriz)
    
    def GradEnt(self, u):
        grado = 0
        for i in range(self.__cant):
            if (self.__matriz[i, u] == 1):
                grado += 1
        print(f"El grado de entrada de {u} es {grado}")
    
    def GradSal(self, u):
        grado = 0
        for i in range(self.__cant):
            if (self.__matriz[u, i] == 1):
                grado += 1
        print(f"El grado de salida de {u} es de {grado}")
    
    def NodoF(self, u):
        i = 0
        while (i < self.__cant) and (self.__matriz[u, i] == 0):
            i += 1
        if (i < self.__cant):
            i = 0
            while (i < self.__cant) and (self.__matriz[i, u] == 0):
                i += 1
            if (i < self.__cant):
                return False
            else:
                return True 
        else:
            return False
    
    def NodoS(self, u):
        i = 0
        while (i < self.__cant) and (self.__matriz[u, i] == 0):
            i += 1
        if (i < self.__cant):
            return False
        else:
            i = 0
            while (i < self.__cant) and (self.__matriz[i, u] == 0):
                i += 1
            if (i < self.__cant):
                return True
            else:
                return False
    
    def Ordenacion_Topologica(self, v, marca):
        marca[v] = True
        for w in self.Adyacentes(v):
            if (marca[w] == False):
                self.Ordenacion_Topologica(w, marca)
        print(f"{v}")