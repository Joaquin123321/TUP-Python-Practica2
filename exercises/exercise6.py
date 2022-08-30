"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
        lista_str = []
        lista_int = []
        lista_ordenada = []
        
        for i in range(0,6):
            if type(lista[i]) == str:
                lista_str.append(lista[i])
            else:
                lista_int.append(lista[i])
        
        lista_ordenada = lista_str + lista_int
        return lista_ordenada


lista = [2, "Hola", 5, 1, "Mundo", 6]

print(numeros_al_final_basico(lista))

"""Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    lista_int = []
    lista_str = []
    lista_auxiliar = [lista_str.append(lista[i]) for i in range(0,6) if type(lista[i]) == str]  
    lista_auxiliar2 = [lista_int.append(lista[i]) for i in range(0,6) if type(lista[i]) == int]

    lista_ordenada = lista_int + lista_str
    print(lista_ordenada)

lista = [2, "Hola", 5, 1, "Mundo", 6]
print(numeros_al_final_comprension(lista))


    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
