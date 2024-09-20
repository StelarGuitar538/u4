class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__izquierda = None
        self.__derecha = None
        
    def getValor(self):
        return self.__valor
    
    def getIzquierda(self):
        return self.__izquierda
    
    def getDerecha(self):
        return self.__derecha
    
    def setIzquierda(self, nodo):
        self.__izquierda = nodo
        
    def setDerecha(self, nodo): 
        self.__derecha = nodo