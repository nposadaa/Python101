# Clase 20: proyecto piedra papel o tijera. Para reactivar esta opción, basta descomentar el bloque
'''
user_option = input('piedra, papel o tijera => ')
user_option = user_option.lower()
pc_option = 'piedra'

if user_option == pc_option:
  print('Empate!')
elif user_option == 'piedra':
  if pc_option == 'tijera':
    print('piedra gana a Tijera!')
    print('user ganó!')
  else:
    print('papel gana a piedra')
    print('PC ganó!')
elif user_option == 'papel':
  if pc_option == 'piedra':
    print('papel gana a piedra')
    print('user ganó!')
  else:
    print('tijera gana a papel')
    print('PC ganó!')
elif user_option == 'tijera':
  if pc_option == 'papel':
    print('tijera gana a papel')
    print('user ganó!')
  else:
    print('piedra gana a tijera')
    print('PC ganó!')
'''

# clase 28: continuación del proyecto de piedra papel o tijera, incluyendo versión con tuplas
#Importamos la función random para usar en el programa
import random

#Esta es una tupla con las opcions para elegir
options = ('piedra', 'papel', 'tijera')

user_option = input('piedra, papel o tijera => ')
user_option = user_option.lower()

#acá usamos la función random sacada de la tupla que declaramos anteriormente.
pc_option = random.choice(options)

#Mostramos las opciones elegidas, y procedemos a evaluar la lógica
print('User option => ', user_option)
print('PC option => ', pc_option)

#Verificamos que la opción del usuario esté o no la opción digitada validando contra la tupla
if not user_option in options:
  print(f'El valor {user_option} no está en las opcions permitidas')

#Decidimos el resultado: Empate, PC gana o user gana.
if user_option == pc_option:
  print('Empate!')
elif user_option == 'piedra':
  if pc_option == 'tijera':
    print('piedra gana a Tijera!')
    print('user ganó!')
  else:
    print('papel gana a piedra')
    print('PC ganó!')
elif user_option == 'papel':
  if pc_option == 'piedra':
    print('papel gana a piedra')
    print('user ganó!')
  else:
    print('tijera gana a papel')
    print('PC ganó!')
elif user_option == 'tijera':
  if pc_option == 'papel':
    print('tijera gana a papel')
    print('user ganó!')
  else:
    print('piedra gana a tijera')
    print('PC ganó!')
