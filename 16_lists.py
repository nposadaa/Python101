# Las listas se crean declarando un variable y listando sus elementos dentro de corchetes cuadrados. Los elementos van separados por ','. Las listas permiten guardar varrios elementos, no sólo números, strings o booleanos.
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make dishes', 'play vids', 'sleep']
print(tasks)

#En las listas también se puede hacer indexing, obteniendo valorese específicos de la lista. Ejemplo, extrayendo el indice 1 de la lista tasks.

print(tasks[1])

#En las listas podemos cambiar valores de los mismos, mutando la lista. Ejemplo abajo cambiando el índice 0.

tasks[0] = 'Watch Netflix'
print(tasks)

#Ejemplo de slicing en una lista de la misma fforma como se hace con srtings pero con los índices de la lista.

print(numbers[:3])

# Uso de operador IN para verifficar existencia de un valor en una lista. Nos devuelve un boleano.
print(2 in numbers)
print('play vids' in tasks)
