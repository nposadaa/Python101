# IF el condicional, que eejecuta la operación True.
if True:
  print('deberia ejecutarse')
  if False:
    print('nunca se ejecuta')

print('\n', '*' * 10, '\n')

# hacemos un ejercicio con una variable obteniada de un input

pet = input('Cuál es tu mascota? Puedes escribir perro o gato: ')

if pet == 'perro':
  print('El perro es el mejor amigo del hombre!')
elif pet == 'gato':
  print('Que asco de mascota!')
else:
  print('no tienes mascota!')

# hacemos un ejemplo con una aplicación de stock para ver el caso else, quee permite evaluar los falsos. Adicional, elif, evalua otro True posible, este se pone antes de llegar al else que evalua los False.

stock = int(input('Cuál es el stock a ingresar?'))

if stock >= 100 and stock <= 1000:
  print('El ingreso es permitido.')
else:
  print('El ingreso NO es permitido!')
