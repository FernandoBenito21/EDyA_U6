from Ponderado_Sec import *
from Ponderado_Enc import *

def Conversor(char):
    if (char == 'A') or (char =='a'):
        num = 0
    elif (char == 'B') or (char =='b'):
        num = 1
    elif (char == 'C') or (char =='c'):
        num = 2
    elif (char == 'D') or (char =='d'):
        num = 3
    elif (char == 'E') or (char =='e'):
        num = 4
    elif (char == 'F') or (char =='f'):
        num = 5
    return num

if __name__=='__main__':
    grafo = Grafo_Ponderado_Sec(6)
    op = 1
    while (op != 0):
        print("Opciones: ")
        print("1.Cargar Grafo")
        print("2.Revisar Costo")
        print("3.Ver grafo")
        print("0.Salir")
        op = int(input('Ingrese una opcion: '))
        if (op == 1):
            continuar = 1
            while (continuar != 0):
                a = input('Ingrese nodo origen: ')
                u = Conversor(a)
                b = input('Ingrese nodo destino: ')
                v = Conversor(b)
                p = int(input('Ingrese peso: '))
                grafo.Insertar(u, v, p)
                continuar = int(input('Continuar? 0 para no, cualquier otro para si: '))
        elif (op == 2):
            a = input('Ingrese el emisor: ')
            u = Conversor(a)
            b = input('Ingrese el destinatario: ')
            v = Conversor(b)
            grafo.Procesa_Dijkstra(u, v)
        elif (op == 3):
            grafo.Mostrar()
            if (isinstance(grafo, Grafo_Ponderado_Sec)):
                grafo.Mostrar_2()
            