from ejercicio1 import Arbol
from nodo import Nodo

def main():
    a = Arbol()
    nuevo = Nodo(10)
    a.insertar(a.getRaiz(), nuevo)
    a.inorden(a.getRaiz())
    
if __name__ == "__main__":
    main()