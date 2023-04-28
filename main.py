from pilas import Pila, Nodo

"""Función de pruebas
"""
def main():
    print('Se crea la pila1:')
    pila = Pila([2,3,4])
    print(pila)
    print('')
    
    print('Se crea la pila2:')
    pila2 = Pila([5,5,6])
    print(pila2.__str__(', '))
    print('')

    print('Se agregan nuevos elementos a la pila1:')
    pila.push([9,8,7])
    print(pila.__str__(' > '))
    print('')

    print('Se elimina un elemento a la pila1:')
    pila.pop()
    print(pila.__str__(' > '))
    print('')

    print('Se elimina 2 elementos a la pila2:')
    pila2.pop(2)
    print(pila2)
    print('')

    print('Se elimina 3 elementos a la pila1:')
    pila.pop(3)
    print(pila.__str__(' > '))
    print('')

if __name__ == '__main__':
    main()