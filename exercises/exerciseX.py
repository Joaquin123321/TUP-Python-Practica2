
from typing import List, Union

###############################################################################


def maximo_recursivo(*args) -> float:
    
    


    
    """Toma una cantidad arbitraria de números y devuelve el mayor.

    Restricciónes:
        - No utilizar la función max
        - No utilizar la ninguna otra función salvo maximo_recursivo
        - Resolver de manera recursiva
    """
lista = [1, 10, 5, -5]
print(maximo_recursivo(lista))

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert maximo_recursivo(1, 10, 5, -5) == 10
    assert maximo_recursivo(4, 9, 18, 6) == 18
    assert maximo_recursivo(24, 9, 18, 20) == 24
    assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce  # noqa: E402


def sumatoria_reduce(n: int) -> int:

    lista = []
    for x in range(0, n, 1):
        lista.append(x)
        lista_definitiva = reduce(lambda x, y: x + y, lista)
    return lista_definitiva


    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar la función reduce.
    Referencia: https://docs.python.org/3/library/functools.html#functools.reduce  # noqa: E501
    """

n = int(input("Ingrese un número: "))
print(sumatoria_reduce(n))

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando la función sorted con una custom key.

    Restricciones:
        - No utilizar bucles.
        - No utilizar comprensiones.
        - Utilizar un lambda.

    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
