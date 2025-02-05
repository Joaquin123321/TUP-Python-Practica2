"""Expresiones Booleanas."""

from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


def es_vocal_if(letra: str) -> bool:
    
    if letra == 'a':
        return True
    if letra == 'e':
        return True
    if letra == 'i':
        return True
    if letra == 'o':
        return True
    if letra == 'u':             
        return True
    return False

letra = str(input("Ingrese una letra: "))
letra = letra.lower()

print(es_vocal_if(letra))

    
"""Toma un string y devuelve un booleano en base a si letra es una vocal o
no.

 Restricciónes:
    - Utilizar un if para cada posibilidad.
    - Utilizar la función lower() sólo una vez.
    - No utilizar ELSE.
    - Utilizar 6 returns.

Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
"""


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
assert es_vocal_if("e")
assert es_vocal_if("E")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    letra = letra.lower()
    if letra in "aeiou":
        return True
    return False
        
letra = str(input("Ingrese una letra: "))


print(es_vocal_if_in(letra))
    
    
    """Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas.

    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations # noqa: E501
    """


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    
    resultado = True
    while not(letra in "aeiou"):
        resultado = False              
        break
    return resultado                                             


letra = str(input("Ingrese una letra: "))
letra = letra.lower() 
    
print(es_vocal_in(letra))  
    
    """Re-escribir como expresión booleana utilizando el operador IN

    Restricciónes:
        - No utilizar IF.
        - Utilizar un único return.
        - No utilizar FOR.
        - No utilizar listas.
    """


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
