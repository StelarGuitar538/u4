from nodito import Nodo

class TAD:
    __raiz: Nodo
    
    def __init__(self):
        self.__raiz = None
        
    def getRaiz(self):
        return self.__raiz
    
    def insertar(self, xraiz, nodo):
        if xraiz == None:
            self.__raiz == nodo
        
        if nodo < xraiz.getValor():
            if xraiz.getIzquierda() == None:
                xraiz.setIzquierda(nodo)
            else:
                self.insertar(xraiz.getIzquierda(), nodo) 
        elif nodo > xraiz.getValor():
            if xraiz.getDerecha() == None:
                xraiz.setDerecha(nodo)
            else:
                self.insertar(xraiz.getDerecha(), nodo)
                
    def buscar(self, xraiz, valor):
        if xraiz == None:
            return None
        elif valor == xraiz.getValor():
            return xraiz
        elif valor < xraiz.getValor():
            return self.buscar(xraiz.getIzquierda(), valor)
        else:
            return self.buscar(xraiz.getDerecha(), valor)
        
    def eliminar(self, xraiz, valor):
        if xraiz == None:
            return None
        elif valor < xraiz.getValor():
            return xraiz.setIzquierda(self.eliminar(xraiz.getIzquierda(), valor))
        elif valor > xraiz.getValor():
            return xraiz.setDerecha(self.eliminar(xraiz.getDerecha(), valor))
        else:
            #nodo hoja
            if xraiz.getDerecha() == None and xraiz.getIzquierda() == None:
                return None
            #nodo con un hijo
            if xraiz.getIzquierda() == None:
                return xraiz.getDerecha()
            elif xraiz.getDerecha() == None:
                return xraiz.getIzquierda()
            sucesor = self.encontrarMin(xraiz.getDerecha())
            xraiz.setValor(sucesor.getValor())
            xraiz.setDerecha(self.eliminar(xraiz.getDerecha(), sucesor.getValor()))
        return xraiz
    
    def encontrarMin(self, xraiz):
        while xraiz.getValor == None:
            return self.encontrarMin(xraiz.getIzquierda())
        return xraiz
    
    def nivel(self, xraiz, valor, nivel):
        if xraiz == None:
            return None
        if valor == xraiz.getValor():
            return nivel
        elif valor < xraiz.getValor():
            return nivel(xraiz.getIzquierda(), valor, nivel+1)
        else:
            return nivel(xraiz.getDerecha(), valor, nivel+1)
        
    def hijo(self, padre, hijo):
        padre = self.buscar(self.__raiz, padre)
        if padre != None: 
            if padre.getIzquierda() != None and padre.getIzquierda() == hijo:
                return True
            elif padre.getDerecha() != None and padre.getDerecha() == hijo:
                return True
            else:
                return False
            
    def padre(self, xraiz, padre, hijo):
        if xraiz == None:
            return False
        if xraiz.getValor() == hijo:
            return padre.getValor() if padre != None else None
        elif xraiz.getValor() < hijo:
            return self.padre(xraiz.getDerecha(), xraiz, hijo)
        else:
            return self.padre(xraiz.getIzquierda(), xraiz, hijo)
        
    def camino(self, valor):
        camino = []
        self.caminoAux(self.__raiz, valor, camino)
        return camino
    
    def caminoAux(self, xraiz, valor, camino):
        if xraiz == None:
            return False
        camino.append(xraiz.getValor())
        if valor == xraiz.getValor():
            return True
        elif valor < xraiz.getValor():
            return self.caminoAux(xraiz.getIzquierda(), valor, camino)
        else:
            return self.caminoAux(xraiz.getDerecha(), valor, camino)
        
    def altura(self, xraiz):
        if xraiz != None:
            izquierda=  self.altura(xraiz.getIzquierda())
            derecha = self.altura(xraiz.getDerecha())
            if derecha > izquierda:
                return derecha +1
            else:
                return izquierda +1
            
    def inorder(self, xraiz):
        if xraiz != None:
            self.inorder(xraiz.getIzquierda())
            print(xraiz.getValor())
            self.inorder(xraiz.getDerecha())