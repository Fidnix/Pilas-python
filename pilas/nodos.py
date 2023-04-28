from typing import Union

"""Es el nodo, una estructura de datos cuyos elementos son: un elemento (dato) u otro nodo (el enlazado)

Args:
    elems (int, list[int], tuple[int]): Son los elementos con los que inicializa los nodos enlazados

Variables:
    _elem (int): Es el dato almacenado
    _sig (Nodo): Es el nodo que sigue al original
"""
class Nodo:
    _elem: int
    _sig: 'Nodo'

    """Función constructora del nodo a partir de uno o más elementos dados

    Parameters:
        elems: Es el entero o iterable de enteros que serán elementos de los nodos
    """
    def __init__(self, elems: Union[int, list[int], tuple[int]] = 0) -> None:
        if(type(elems)==int):
            self._elem = elems
            self._sig = None
            return

        self._elem = elems[-1]
        self._sig = None
        for elem in elems[:-1]:
            nuevo_nodo = Nodo(elem)
            nuevo_nodo._sig = self._sig
            self._sig = nuevo_nodo

    """Devuelve un string que contiene a los elementos de la pila al tratar de convertir a la pila en string

    Parameters:
        sep: Es el separador entre los elementos

    Returns:
        output: es el string con cada elemento de la pila
    """

    def __str__(self, sep: str = ' ') -> str:
        output = ''
        current_node = self
        while(current_node != None):
            output += f'{sep}{current_node._elem}'
            current_node = current_node._sig
        return output[len(sep):]