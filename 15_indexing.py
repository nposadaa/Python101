# A continuación la clase de indexing.
print('EJEMPLOS DE INDEXING', '\n')
text = 'Nico sabe Python'
print(
  text[0]
)  #extraemos la posición 0, o sea la N. En python la posición inicial es 0.
print(text[1])  #extraemos la posición 1, o sea la i.
# print(text[999])  nos daría un error de syntax pq no exist dicha posición.
size = len(text)
print('size => ', size)
print(
  text[size - 1]
)  #Para imprimir la úlima posición, debemos calcularla. Primeero calculamos con función len, guardamos en una variable, y ponemos dicha variable como parametro del index en el print. Notar que debemos restar 1, dado que LEN cuenta desde 1 preo sabemos que los índices empiezan desde 0, así que si el largo es 16, en reaelidad la última posición por índice es 15.
print(
  text[-1]
)  #esta es la alternativa fácil de python al cálculo anteerior, para python el index con menos es el string empezando desde la úlima posición.

#A continuación la clase de Slicing.
print('\n', 'EJEMPLOS DE SLICING', '\n')

print(text[0:4])  #sacamos los caracterres en las posiciones 0 a la 4.
print(
  text[:10]
)  #cuando obviamos el printer caracter antes de los dos puntos, se entiende que es 0.
print(
  text[10:]
)  # de igual forma, si dejamos el final vacio después de los dos puntos, iría hasta el final.
print(
  text[10:16:2]
)  # El tercer argumento del slicing es el número de saltos, es decir, en este ejemplo tomamos la palabra Python de la 10 a la 16, pero con dos saltos, imprimirá la primera letra de la posición, luego saltará a la tercera letra, y así. escribiendo Pto y no Python.
print(text[::2])  #Mismo ejemplo con toda la string y dos saltos.
