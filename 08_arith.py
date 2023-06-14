#print de una operación aritmética nos mostrará el resultado de la misma sin necesidad de crear un variable para alojar el resultado
# with int y float, realiza las operaciones matemáticas
#addition
print(10 + 10)
#substraction
print(10 - 5)
#multiplication
print(10 * 2)
#division
print(10 / 2)
#con strings replica y une las cadenas.
print('hola' + ' mundo')
print('hola' * 3)
#print('hola' / 2) division no se puede hacer con srtings.

#division de módulo o residuo.
print(10 / 3)
print(10 % 3)  #el residuo es 1

#division con valor entero de una division descartando los decimales
print(10 // 3)

#exponenciación a un número x
print(2**3)  #2 elevado a 3, es 8

#ecuaciones largas, según las regla PEMDAS:
# P - parenthesis
# E - exponentiation
# M - multiplication
# D - division
# A - adittion
# S - sustraction
print(
  2**3 + 3 - 7 / 1 // 4
)  # para resolver primero la exponencial da (2**3) == 8, luego las divisiones de la derecha dan 1.75, pero por ser de entero es 1. Luego la suma 8 + 3, y luego la resta de 1 == 10.
