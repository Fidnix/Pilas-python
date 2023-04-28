from pilas.nodos import Nodo
from typing import Union

"""Establece un inicio entre los nodos y contiene informacion sobre sus longitudes, a parte de permitir las unicas operaciones: push y pop

Args:
    elems (int, list[int], tuple[int]): Los datos con los que inicializara la pila; por defecto sera None

Variables:
    _size (int): Longitud de los nodos de la pila
    _size (Nodo): Inicio de los nodos
"""
class Pila:
    _size: int
    _cabeza: Nodo

    """Construye la pila.

    Parameters:
        Elems: Un entero o una lista de enteros
    """
    def __init__(self, elems: Union[int, list[int], tuple[int]] = None) -> None:
        if(elems == None):
            self._size = 0
            self._cabeza = None
            return
        self._cabeza = Nodo(elems)
        if(type(elems) == int):
            self._size = 1
            return
        self._size = len(elems)

    """Verifica si la lista es vacia
    Return:
        bool
    """
    def empty_pile(self):
        return self._size == 0

    """Devuelve un string con formato aplicado a la pila si se pide que la pila se convierta en str

    Parameters:
        sep: separador entre los elementos
    Return:
        string
    """
    def __str__(self, sep: str = ' ') -> str:
        output = ''
        current_node = self._cabeza
        for _ in range(0, self._size):
            output += f'{sep}{current_node._elem}'
            current_node = current_node._sig
        return output[len(sep):]
    
    """Construye la pila.

    Parameters:
        Elems: Un entero o una lista de enteros
    """
    def push(self, elems: Union[int, list[int], tuple[int]] = 0) -> None:
        prev_node = self._cabeza 
        self._cabeza = Nodo(elems)

        if(self.empty_pile()):
            return
        
        current_node = self._cabeza
        while(current_node._sig != None):
            current_node = current_node._sig
        current_node._sig = prev_node

        if(type(elems) == int):
            self._size += 1
            return
        self._size += len(elems)

    """Devuelve y elimina los n ultimos elementos de la pila

    Parameters:
        n: Entero que representa el numero de elementos a eliminar

    Returns:
        aux_tuple: Tupla de los n últimos elementos
    """
    def pop(self, n: int = 1) -> tuple[int]:
        if(self.empty_pile()):
            return None
        if( n < 1 or n > self._size):
            raise Exception('Error: El n debe estar en el rango de cantidad de elementos de la pila')
        
        aux_tuple = tuple()
        
        for _ in range(0, n):
            aux_tuple += (self._cabeza._elem,)
            self._cabeza = self._cabeza._sig
        self._size -= n
        return aux_tuple