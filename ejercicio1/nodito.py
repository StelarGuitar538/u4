class Nodo:
    __valor: int
    __derecha: None
    __izquierda: None
    
    def __init__(self, valor):
        self.__valor = valor
        self.__derecha = None
        self.__izquierda = None
        
    def getValor(self):
        return self.__valor
    
    def getDerecha(self):
        return self.__derecha
    
    def getIzquierda(self):
        return self.__izquierda
    
    def setValor(self, valor):
        self.__valor = valor
        
    def setIzquierda(self, izq):
        self.__izquierda = izq
        
    def setDerecha(self, der):
        self.__derecha = der
        
    def grado(self):
        if self.__izquierda == None and self.__derecha == None:
            return 0
        elif self.__izquierda == None and self.__derecha != None:
            return 1
        elif self.__izquierda != None and self.__derecha == None:
            return 1
        else:
            return 2