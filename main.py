# Clase 20: proyecto piedra papel o tijera

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