import math

class NodoB:
    def __init__(self, es_hoja=False):
        self.es_hoja = es_hoja  # Determina si el nodo es una hoja
        self.claves = []        # Almacena las claves (valores) del nodo
        self.hijos = []         # Almacena los hijos del nodo

class ArbolB:
    def __init__(self, grado):
        self.grado = grado  # Grado máximo del árbol (máximo número de hijos por nodo)
        self.raiz = NodoB(True)  # Inicialmente el árbol tiene solo la raíz, que es hoja

    # Método para dividir un nodo cuando está lleno
    def dividirNodo(self, nodo, i, hijo):
        nuevoNodo = NodoB(hijo.es_hoja)
        nuevoNodo.claves = hijo.claves[self.grado // 2:]  # Extraer claves del nodo lleno

        # Si el nodo no es hoja, también tenemos que dividir sus hijos
        if not hijo.es_hoja:
            nuevoNodo.hijos = hijo.hijos[self.grado // 2:]

        # Reducir el número de claves del nodo dividido
        hijo.claves = hijo.claves[:self.grado // 2]
        hijo.hijos = hijo.hijos[:self.grado // 2 + 1]

        # Insertar el nuevo hijo en el nodo padre
        nodo.hijos.insert(i + 1, nuevoNodo)
        nodo.claves.insert(i, hijo.claves.pop())  # Subir la clave del medio al nodo padre

    # Método para insertar una nueva clave en el árbol
    def insertar(self, clave):
        raiz = self.raiz

        # Si la raíz está llena, dividimos y creamos una nueva raíz
        if len(raiz.claves) == self.grado - 1:
            nuevaRaiz = NodoB(False)  # Crear una nueva raíz
            nuevaRaiz.hijos.append(self.raiz)  # La antigua raíz es ahora el primer hijo
            self.dividirNodo(nuevaRaiz, 0, self.raiz)  # Dividir el nodo
            self.raiz = nuevaRaiz  # La nueva raíz se convierte en la raíz del árbol

        # Llamar al método auxiliar de inserción
        self._insertarNoLleno(self.raiz, clave)

    # Método auxiliar para insertar cuando el nodo no está lleno
    def _insertarNoLleno(self, nodo, clave):
        if nodo.es_hoja:
            # Insertar la clave en la posición adecuada
            i = len(nodo.claves) - 1
            nodo.claves.append(None)  # Añadir espacio para la nueva clave
            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = clave
        else:
            # Buscar el hijo donde debemos insertar
            i = len(nodo.claves) - 1
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1

            # Si el hijo está lleno, lo dividimos
            if len(nodo.hijos[i].claves) == self.grado - 1:
                self.dividirNodo(nodo, i, nodo.hijos[i])

                # Después de la división, debemos decidir cuál de los dos hijos tomar
                if clave > nodo.claves[i]:
                    i += 1

            # Insertar en el hijo adecuado
            self._insertarNoLleno(nodo.hijos[i], clave)

    # Recorrido inorden del árbol
    def recorrerInorden(self, nodo=None, resultado=None):
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []

        i = 0
        while i < len(nodo.claves):
            # Si no es hoja, recorrer el subárbol izquierdo
            if len(nodo.hijos) > 0:
                self.recorrerInorden(nodo.hijos[i], resultado)
            resultado.append(nodo.claves[i])
            i += 1

        # Recorrer el último subárbol si existe
        if len(nodo.hijos) > 0:
            self.recorrerInorden(nodo.hijos[i], resultado)

        return resultado

# Función principal para probar el Árbol B
if __name__ == "__main__":
    arbol = ArbolB(grado=3)  # Crear un árbol B de grado 3

    # Insertar valores en el árbol B
    valores = [10, 20, 5, 6, 12, 30, 7, 17]
    for valor in valores:
        arbol.insertar(valor)

    # Recorrer y mostrar los valores en orden
    print("Recorrido inorden del árbol B:", arbol.recorrerInorden())
