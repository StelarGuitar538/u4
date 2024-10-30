from nodito import Nodo

class TAD:
    __raiz: Nodo
    
    def __init__(self):
        self.__raiz = None
        
    def getRaiz(self):
        return self.__raiz
    
    def insertar(self, xraiz, valor):
        if xraiz == None:
            self.__raiz = valor
        else:
            if valor < xraiz.getValor():
                if xraiz.getIzquierda() == None:
                    xraiz.setIzquierda(valor)
                else:
                    self.insertar(xraiz.getIzquierda(), valor)
            elif valor > xraiz.getValor():
                if xraiz.getDerecha() == None:
                    xraiz.setDerecha(valor)
                else:
                    self.insertar(xraiz.getDerecha(), valor)
    
    def buscar(self, xraiz, valor):
        if xraiz != None:
            if valor == xraiz.getValor():
                return xraiz
            elif valor < xraiz.getValor():
                return self.buscar(xraiz.getIzquierda(), valor)
            else:
                return self.buscar(xraiz.getDerecha(), valor)
            
    def eliminar(self, xraiz, valor):
        if xraiz != None:
            if valor < xraiz.getValor():
                return xraiz.setIzquierda(self.eliminar(xraiz.getIzquierda(), valor))
            elif valor > xraiz.getValor():
                return xraiz.setDerecha(self.eliminar(xraiz.getDerecha(), valor))
            else:
                if xraiz.getDercha() == None and xraiz.getIzquierda() == None:
                    return None
                if xraiz.getDerecha() == None and xraiz.getIzquierda() != None:
                    return xraiz.getIzquierda()
                elif xraiz.getDerecha != None and xraiz.getIzquierda() == None:
                    return xraiz.getDerecha()
                sucesor = self.min(xraiz.getDerecha())
                xraiz.setValor(sucesor.getValor())
                xraiz.setDerecha(self.eliminar(xraiz.getDerecha, sucesor.getValor()))
                
                
    def min(self, xraiz):
        if xraiz != None:
            if xraiz.getIzquierda() != None:
                return self.min(xraiz.getIzquierda())
            return xraiz
            
            
    def nivel(self, xraiz, valor, nivel):
        if xraiz != None:
            if valor == xraiz.getValor():
                return nivel
            elif valor < xraiz.getValor():
                return self.nivel(xraiz.getIzquierda(), valor, nivel +1)
            else:
                return self.nivel(xraiz.getDerecha(), valor, nivel +1)
            
    def hoja(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo.getIzquierda() == None and nodo.getDerecha() == None:
            print(f"el nodo {nodo} es hoja")
        else:
            print(f"el nodo {nodo} no es hoja")
            
    def hijo(self, padre, hijo):
        padre = self.buscar(self.__raiz, padre)
        if padre != None:
            if padre.getDerecha() == hijo or padre.getIzquierda() == hijo:
                return True
            else:
                return False
            
    def padre(self, xraiz, padre, hijo):
        if xraiz != None:
            if xraiz.getValor() == hijo:
                return padre if padre != None else None
            elif hijo < xraiz.getValor():
                return self.padre(xraiz.getIzquierda(), xraiz, hijo)
            else:
                return self.padre(xraiz.getDerecha(), xraiz, hijo)
            
    def camino(self, valor):
        camino = []
        self.caminoAux(self.__raiz, camino, valor)
        return camino
    
    def caminoAux(self, xraiz, camino, valor):
        if xraiz != None:
            camino.append(xraiz.getValor())
            if valor == xraiz.getValor():
                return True
            elif valor < xraiz.getValor():
                return self.caminoAux(xraiz.getIzquierda(), camino, valor)
            else:
                return self.caminoAux(xraiz.getDerecha(), camino, valor)
                
    def altura(self, xraiz):
        if xraiz != None:
            izq = xraiz.getIzquierda()
            der = xraiz.getDerecha()
            if der > izq:
                return der + 1
            else:
                return izq +1
            
    def inorder(self, xraiz):
        if xraiz != None:
            self.inorder(xraiz.getIzquierda())
            print(xraiz.getValor())
            self.inorder(xraiz.getDerecha())
            
    def contarNodos(self, xraiz):
        if xraiz != None:
            return 1 + self.contarNodos(xraiz.getDerecha()) + self.contarNodos(xraiz.getIzquierda())
        
    def mostrarSucesores(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo != None:
            print(f"sucesores de {valor}")
            return self.inorder(nodo)
        
    def mostrarFrontera(self, xraiz):
        if xraiz != None:
            self.mostrarFrontera(xraiz.getIzquierda())
            if xraiz.grado() == 0:
                print(xraiz.getValor())
            self.mostrarFrontera(xraiz.getDerecha())
    
