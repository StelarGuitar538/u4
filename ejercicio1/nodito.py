class Nodo:
    __valor: int
    __izquierda: None
    __derecha: None
    
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
    
    def setValor(self, valor):
        self.__valor = valor
        
    def setIzquierda(self, i):
        self.__izquierda = i
        
    def setDerecha(self, d):
        self.__derecha = d
        
    def grado(self):
        if self.__derecha == None and self.__izquierda == None:
            return -1
        elif self.__izquierda == None and self.__derecha != None:
            return 1
        elif self.__derecha == None and self.__izquierda != None:
            return 1
        elif self.__izquierda != None and self.__derecha != None:
            return 2