# las tuplas son como las listas, pero a diferencia de ellas no se pueden modificar, tal como las strings. Su sintaxis es con paréntesis  (), opuesto a la lista que es con corchete recto []. Al no poder modificarse las tuplas no se dejan modificar usando métodos, como append o cambiar indices
numbers = (1, 2, 3, 4)
strings = ('nico', 'sebas', 'vero', 'nico')

print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

#El acceso a los valores de las tuplas es igúal que con las listas, usando los índices

print('Indice 0 => ', numbers[0])
print('Indice -1 => ', numbers[-1])

#Podemos buscar valores deentro de las tuplas igual que con las listas

print(strings)
print(strings.index('sebas'))

#Contar ocurrencias de valores

print(strings.count('nico'))

#Es posible convertir tuplas a listas, con una simple declaración

my_list = list(strings)
print(my_list)
print(type(my_list))

#Luego de hacer modificaciones en la lista, podemos volver a convertirla en tupla.

my_list[0] = 'nicolas'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))