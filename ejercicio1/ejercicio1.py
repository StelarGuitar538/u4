from nodo import Nodo

class Arbol:
    def __init__(self):
        self.__raiz = None
        
    def insertar(self, valor):
        if self.__raiz == None:
            self.__raiz = Nodo(valor)
        else:
            self.insertarAux(self.__raiz, valor)
            
    def insertarAux(self, nodo, valor):
        if valor < nodo.getValor():
            if nodo.getIzquierda() == None:
                nodo.setIzquierda(Nodo(valor))
            else:
                self.insertarAux(nodo.getIzquierda(), valor)
        elif valor > nodo.getValor():
            if nodo.getDerecha() == None:
                nodo.setDerecha(Nodo(valor))
            else:
                self.insertarAux(nodo.getDerecha(), valor)
                
    def buscar(self, valor):
        if self.__raiz == None:
            return None
        else:
            return self.buscarAux(self.__raiz, valor)
        
    def buscarAux(self, nodo, valor):
        if nodo.getValor() == valor:
            return nodo
        elif valor < nodo.getValor():
            return self.buscarAux(nodo.getIzquierda(), valor)
        else:
            return self.buscarAux(nodo.getDerecha(), valor)
        
    def eliminar(self, valor):
        if self.__raiz == None:
            return
        else:
            self.eliminarAux(self.__raiz, valor)
            
    def eliminarAux(self, nodo, valor):
        if valor < nodo.getValor():
            nodo.setIzquierda(self.eliminarAux(nodo.getIzquierda(), valor))
        elif valor > nodo.getValor():
            nodo.setDerecha(self.eliminarAux(nodo.getDerecha(), valor))
        else:
            #caso 1: simplemente elimino el nodo
            if nodo.getIzquierda() == None and nodo.getDerecha() == None:
                return None
            #caso 2: el nodo se elimina y su hijo ocupa el lugar vacio
            if nodo.getIzquierda() == None:
                return nodo.getDerecha()
            elif nodo.getDerecha() == None:
                return nodo.getIzquierda()
            #caso 3: se encuentra el sucesor inorden(el nodo mas pequeno en el subarbol derecho) o el predecesor inorden (el nodo mas grande en ek subarbol izquierdo) para reemplazar el nodo eliminado
            sucesor = self.encontrarMin(nodo.getDerecha())
            nodo.getValor() = sucesor.getValor()
            nodo.getDerecha() = self.eliminarAux()
        return nodo
    
    def encontrarMin(self, nodo):
        actual = nodo
        while actual.getIzquierda() == None:
            actual = actual.getIzquierda()
        return actual
    
    def nivel(self, valor):
        return self.nivelAux(self.__raiz, valor, 0)
    
    def nivelAux(self, nodo, valor, nivel):
        if nodo == None:
            return -1 #si no encuentra el nodo
        if nodo.getValor() == valor:
            return nivel
        elif valor < nodo.getValor():
            return self.nivelAux(nodo.getIzquierda(), valor, nivel+1)
        else:
            return self.nivelAux(nodo.getDerecha(), valor, nivel +1)
        
    def hoja(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo == None:
            return nodo.getIzquierda() == None and nodo.getDerecha() == None:
        return False
    
    