class Nodo:
    def __init__(self, dato):
        self.__item = dato
        self.__sig = None

    def getItem(self):
        return self.__item

    def setItem(self, unItem):
        self.__item = unItem
    
    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig
    
class Reg_Dijkstra:
    __conocido : bool
    __camino : int
    __distancia : int
    
    def __init__(self):
        self.__conocido = False
        self.__camino = -1
        self.__distancia = float('inf')
    
    def getConocido(self):
        return self.__conocido
    
    def getCamino(self):
        return self.__camino
    
    def getDistancia(self):
        return self.__distancia
    
    def setConocido(self, x):
        self.__conocido = x
    
    def setCamino(self, x):
        self.__camino = x
    
    def setDistancia(self, x):
        self.__distancia = x

class Vertice_Ponderado:
    def __init__(self, dato, p):
        self.__dato = dato
        self.__sig = None
        self.__peso = p
    
    def getDato(self):
        return self.__dato

    def setDato(self, unItem):
        self.__dato= unItem
    
    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig
    
    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = peso