# CRUD: Create, Read, Update & Delete. Estas son las operacions que see debe poder realizar en una lista.

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[1])

# Update the last position (remember negative are from end to the start)

numbers[-1] = 10
print(numbers)

# .append es un método que sirve para agregar nuevos elementos al final de la lista. Los métodos por sintaxis se escriben con . y el método después de la lista.

numbers.append(700)
print(numbers)

# .insert inserta un valor en el índice que le indiquemos, seguido por el valor a insertar. Esto creará nuevos índices para toda la lista.

numbers.insert(0, 'hola')
print(numbers)
numbers.insert(3, 'change')
print(numbers)

# fusión de listas en nuevas listas, con tan sólo sumarlas

tasks = ['todo 1', 'todo 2', 'todo 3']
print(tasks)
new_list = numbers + tasks
print(new_list)

# para averiguar él índice de un valor específico, usamos el método .index y entregamos el valor a buscar. Esto lo usamos como queramos, en l caso abajo lo guardamos en una variable para ver dónde está

index_todo2 = new_list.index('todo 2')
print('índice de todo 2 es => ', index_todo2)
# en este caso, usamos la variable que guardó el índice del valor buscado como input para cambiar dicho índice con un valor nuevo
new_list[index_todo2] = 'todo 2 changed'
print(new_list)

# .remove removerá el elemento que le indiquemos con el valor.

new_list.remove('todo 1')
print(new_list)

# .pop elimina el último elemento de la lista por defecto, sin embargo, también le podemos dar índices que queramos eliminar especificamente.

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

# .reverse transforma toda la lista reversando por completo los índices

new_list.reverse()
print(new_list)

# .sort órdena la lista según la instrucción que le demos. En el ejemplo abajo la lista fue definida en desorden numérico, el sort ordena de forma ascendente por deffecto. Sort no funciona cuando hay typos combinados en la misma lista.

numbers_a = [1, 10, 5, 15]
print(numbers_a)
numbers_a.sort()
print(numbers_a)