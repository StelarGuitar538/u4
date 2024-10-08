class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # Altura inicial del nodo

class ArbolAVL:
    # Obtener la altura de un nodo
    def obtenerAltura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    # Obtener el factor de balance de un nodo
    def obtenerBalance(self, nodo):
        if not nodo:
            return 0
        return self.obtenerAltura(nodo.izquierdo) - self.obtenerAltura(nodo.derecho)

    # Rotación a la derecha
    def rotacionDerecha(self, y):
        x = y.izquierdo
        T2 = x.derecho

        # Realizar la rotación
        x.derecho = y
        y.izquierdo = T2

        # Actualizar alturas
        y.altura = max(self.obtenerAltura(y.izquierdo), self.obtenerAltura(y.derecho)) + 1
        x.altura = max(self.obtenerAltura(x.izquierdo), self.obtenerAltura(x.derecho)) + 1

        # Retornar nueva raíz
        return x

    # Rotación a la izquierda
    def rotacionIzquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo

        # Realizar la rotación
        y.izquierdo = x
        x.derecho = T2

        # Actualizar alturas
        x.altura = max(self.obtenerAltura(x.izquierdo), self.obtenerAltura(x.derecho)) + 1
        y.altura = max(self.obtenerAltura(y.izquierdo), self.obtenerAltura(y.derecho)) + 1

        # Retornar nueva raíz
        return y

    # Insertar un nuevo valor en el árbol AVL
    def insertar(self, nodo, valor):
        # Realizar la inserción normal en un árbol binario de búsqueda
        if not nodo:
            return NodoAVL(valor)
        elif valor < nodo.valor:
            nodo.izquierdo = self.insertar(nodo.izquierdo, valor)
        else:
            nodo.derecho = self.insertar(nodo.derecho, valor)

        # Actualizar la altura del nodo padre
        nodo.altura = 1 + max(self.obtenerAltura(nodo.izquierdo), self.obtenerAltura(nodo.derecho))

        # Obtener el factor de balance para ver si el nodo está desbalanceado
        balance = self.obtenerBalance(nodo)

        # Caso 1: Rotación a la derecha si el árbol está desbalanceado hacia la izquierda
        if balance > 1 and valor < nodo.izquierdo.valor:
            return self.rotacionDerecha(nodo)

        # Caso 2: Rotación a la izquierda si el árbol está desbalanceado hacia la derecha
        if balance < -1 and valor > nodo.derecho.valor:
            return self.rotacionIzquierda(nodo)

        # Caso 3: Rotación izquierda-derecha
        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self.rotacionIzquierda(nodo.izquierdo)
            return self.rotacionDerecha(nodo)

        # Caso 4: Rotación derecha-izquierda
        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self.rotacionDerecha(nodo.derecho)
            return self.rotacionIzquierda(nodo)

        return nodo

    # Recorrido inorden del árbol (izquierda -> raíz -> derecha)
    def recorrerInorden(self, nodo):
        if not nodo:
            return []
        return self.recorrerInorden(nodo.izquierdo) + [nodo.valor] + self.recorrerInorden(nodo.derecho)

# Función principal para probar el árbol AVL
if __name__ == "__main__":
    arbol = ArbolAVL()
    raiz = None

    # Insertar valores en el árbol
    valores = [10, 20, 5, 6, 3, 9, 15]
    for valor in valores:
        raiz = arbol.insertar(raiz, valor)

    # Recorrer y mostrar los valores en orden
    print("Recorrido inorden del árbol AVL:", arbol.recorrerInorden(raiz))
