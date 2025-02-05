"""For, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    suma = 0
    for i in range(1, n):
        suma = suma + i
    return suma


n = int(input("Ingresar un número: "))
print(sumatoria_basico(n))


"""Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """
# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    suma = list(range(n), n)
    return sum(suma)


n = int(input("Ingresar un número: "))
print(sumatoria_sum)

"""Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """
# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402


def multiplicar_basico(numeros: Iterable[float]) -> float:
    producto = 1
    if not(numeros):
        return 0

    for i in range(numeros[0], numeros[-1]+1):
        producto = producto * i
    return producto
    


numeros = [5, 6, 7, 8, 9]

print(multiplicar_basico(numeros))
print(multiplicar_basico([]))

    """Toma un lista de números y devuelve el producto de todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """

# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN
