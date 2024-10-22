from Nodos import Nodo

class Pila_Encadenada:
        __cabeza : object
        def __init__(self):
            self.__cabeza = None
            self.__cant = 0
        
        def Vacia(self):
            return self.__cabeza == None
        
        def Insertar(self, x):
            Elemento = Nodo(x)
            Elemento.setSig(self.__cabeza)
            self.__cabeza = Elemento
            self.__cant += 1
        
        def Suprimir(self):
            retorna = -1
            if self.Vacia() == False:
                retorna = self.__cabeza.getItem()
                self.__cabeza = self.__cabeza.getSig()
                self.__cant -= 1
            else:
                print ("La pila esta vacia \n")
            return retorna
        
        def Recorrer(self):
            x = self.__cabeza
            while (x != None):
                print("{}".format(x.getItem()))
                x = x.getSig()
            return None