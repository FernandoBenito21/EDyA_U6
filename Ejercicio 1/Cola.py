from Nodos import Nodo

class Cola_Encadenada:
        __primero : object
        __ultimo : object
        __cant : int
        def __init__(self):
            self.__cant = 0
            self.__primero = None
            self.__ultimo = None
        
        def Vacia(self):
            return self.__cant == 0
        
        def Insertar(self, x):
            Elemento = Nodo(x)
            if (self.__ultimo == None):
                self.__primero = Elemento
            else:
                self.__ultimo.setSig(Elemento)
            self.__ultimo = Elemento
            self.__cant += 1
        
        def Suprimir(self):
            retorna = None
            if (self.Vacia() == False):
                retorna = self.__primero.getItem()
                self.__primero = self.__primero.getSig()
                self.__cant -= 1
                if (self.__primero == None):
                    self.__ultimo = None
            else:
                print("Tenes la cola vacia")
            return retorna
        
        def Recorrer(self):
            aux = self.__primero
            while(aux != None):
                print(f"{aux.getItem()}")
                aux = aux.getSig()