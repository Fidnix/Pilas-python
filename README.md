# Pilas en python

Este proyecto es una implementación personal y educativa de las pilas aplicadas en python; por lo que puedes copiarlo como si fuera StackOVerFlow

# Estructura de los archivos

```
.
├── main.py
├── pilas
│   ├── __init__.py
│   ├── nodos.py
│   └── pilas.py
└── README.md
```

* main: Es el archivo de prueba para las pilas
* pilas/init: Es el archivo que exporta las clases necesarias a modulos padre
* pilas/nodos: Contiene las funcionalidades basicas de los nodos(constructor e impresion)
* pilas/pilas: Usa las funcionalidades de los nodos para crear las listas

# Funcionalidades de las pilas

* push(elems): Añade elementos, puede ser una lista
* pop(n): Devuelve y elimina elementos, puede eliminar un número n de elementos y devolverlos como tupla
* str: función intrínseca de las clases, sirve para darle formato a las salidas en consola de la pila
    > Note que:
    > ```
    > print(pila)
    > ```
    > 
    > Es lo mismo que:
    > ```
    > print(pila.__str__())
    > ```

# Motivacion de este proyecto

* Mi mama
* No reprobar EDPM