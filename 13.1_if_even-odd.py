numero = int(input('Ingresa un número: '))

reciduo = numero % 2

if reciduo == 0:
  print(
    f'El número {numero} es par dado su reciduo {reciduo} de división por 2')
else:
  print(
    f'El número {numero} es impar dado su reciduo {reciduo} de división por 2')
