from nodo import Nodo

class Arbol:
    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz
    
    def insertar(self,raiz, nodo):
        if raiz == None:
            self.__raiz = nodo
        
        elif nodo.getValor() < raiz.getValor():
            if raiz.getIzquierda() == None:
                raiz.setIzquierda(nodo)
            else:
                self.insertar(raiz.getIzquierda(), nodo)
        elif nodo.getValor() > raiz.getValor():
            if raiz.getDerecha() == None:
                raiz.setDerecha(nodo)
            else:
                self.insertar(raiz.getDerecha(), nodo)
    
    
                
    def buscar(self,nodo, valor):
        if self.__raiz == None:
            return None
        elif nodo.getValor() == valor:
            return nodo
        elif valor < nodo.getValor():
            return self.buscarAux(nodo.getIzquierda(), valor)
        else:
            return self.buscarAux(nodo.getDerecha(), valor)
        
        
    def eliminar(self, nodo, valor):
        if self.__raiz == None:
            return
        if valor < nodo.getValor():
            nodo.setIzquierda(self.eliminar(nodo.getIzquierda(), valor))
        elif valor > nodo.getValor():
            nodo.setDerecha(self.eliminar(nodo.getDerecha(), valor))
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
            sucesor = self.encontrarMin(nodo.getDerecha()) #encuentra el sucesor inorden
            nodo.getValor() = sucesor.getValor() #reemplaza el nodo eliminado por el sucesor inorden
            nodo.getDerecha() = self.eliminar() #elimina el sucesor inorden
        return nodo
    
    def encontrarMin(self, nodo):
        actual = nodo
        while actual.getIzquierda() == None:
            actual = actual.getIzquierda()
        return actual
    
    def nivel(self, nodo, valor, nivel):
        if nodo == None:
            return -1 #si no encuentra el nodo
        if nodo.getValor() == valor:
            return nivel
        elif valor < nodo.getValor():
            return self.nivel(nodo.getIzquierda(), valor, nivel+1)
        else:
            return self.nivel(nodo.getDerecha(), valor, nivel +1)
        
    def hoja(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo == None:
           return False
        return nodo.getIzquierda() == None and nodo.getDerecha() == None
    
    def hijo(self, padre, hijo):
        padre = self.buscar(self.__raiz, padre)
        if padre != None:
            if padre.getIzquierda() != None and padre.getIzquierda().getValor() == hijo:
                return True
            elif padre.getDerecha() != None and padre.getDerecha().getValor() == hijo:
                return True
        return False
    
    def padre(self, nodo, hijo, padre):
        if nodo == None:
            return False
        elif nodo.getValor() == hijo:
            return padre.getValor() if padre != None else None 
        elif hijo < nodo.getValor():
            return self.padre(nodo.getIzquierda(), hijo, nodo)
        else:
            return self.padre(nodo.getDerecha(), hijo, nodo)
        
    def camino(self,valor):
        camino = []
        self.caminoAux(self.__raiz, valor, camino)
        return camino
    
    def caminoAux(self, nodo, valor, camino):
        if nodo == None:
            return False
        camino.append(nodo.getValor())
        if nodo.getValor() == valor:
            return True
        elif valor < nodo.getValor():
            return self.caminoAux(nodo.getIzquierda(), valor, camino)
        else:
            return self.caminoAux(nodo.getDerecha(), valor, camino)
        
    def altura(self, nodo):
        if nodo == None:
            return -1
        else:
            alturaIzquierda = self.altura(nodo.getIzquierda())
            alturaDerecha = self.altura(nodo.getDerecha())
            return max(alturaIzquierda, alturaDerecha) + 1
        
    def inorden(self, nodo):
        if nodo != None:
            self.inorden(nodo.getIzquierda())
            print(nodo.getValor())
            self.inorden(nodo.getDerecha())
            
    def preorden(self, nodo):
        if nodo != None:
            print(nodo.getValor())
            self.preorden(nodo.getIzquierda())
            self.preorden(nodo.getDerecha())
            
    def postorden(self, nodo):
        if nodo != None:
            self.postorden(nodo.getIzquierda())
            self.postorden(nodo.getDerecha())
            print(nodo.getValor())