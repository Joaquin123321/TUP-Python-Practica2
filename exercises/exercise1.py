"""Bloque IF, operadores lógicos, función max y operador ternario."""


def maximo_basico(a: float, b: float) -> float:
    mayor = a
    if b > a:
        mayor = b
    print(mayor)     

a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))

maximo_basico(a, b)
   
   
   
    """Toma dos números y devuelve el mayor.
    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
    """


# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_libreria(a: float, b: float) -> float:
     print(max(a,b))
        

a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))

maximo_libreria(a,b)


"""Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """

# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    mayor_numero = "Número 1" if a > b else "Número 2"
    print("El mayor número es el", mayor_numero)

a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))

maximo_ternario(a,b)

    
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """


# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
