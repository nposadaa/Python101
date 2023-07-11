#Un diccionario tiene una llave un descriptor para la llave. Su sintaxis se hace definiendo una variable con corchetes al lado derecho de la igualdad

my_dict = {}
print(type(my_dict))

my_dict = {'avion': '747', 'name': 'Nicolás', 'last_name': 'Posada', 'age': 36}
print(my_dict)

#si hacemos un len, nos entreegará el número de valores más no el largo de cada uno.
print(len(my_dict))

#podemos hacer siling de valores usando la llave. Esto imprimirá el descriptor de la llave buscada. Es decir, age, imprimirá eel valor de edad, mas no el valor "age"
print(my_dict['age'])
print(my_dict['last_name'])

#podemos hacer lo mismo con el método .get, y adicional este método si no existee el valor será capaz de hacer un handling, mientras que el slicing fallará por runtime.

print(my_dict.get('unvalor'))
print(my_dict.get('age'))