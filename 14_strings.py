#Todos los ejercicios abajo se basan en la variable text que contiene el siguiente texto declarado:
text = 'nico sabe programar en python'

# Uso del operador IN para buscar substrings
print('JavaScript' in text)
print('Python' in text)
if 'Python' in text:
  print('Buen lenguaje!')
else:
  print('Elige un lenguaje!')

# Uso de la función LEN para medir tamaño de los strings. Los espacios cuentan!

size = len(text)
print(size)

#uso de subinstrucciones para cambiar a mayúsculas, minúsculas, proper, etc

print(text.upper())
print(text.lower())
print(text.count('a'))  #cuenta las ocurrencias del caracter en el string.
print(text.swapcase())  #cambia de mayus a minus, y viceversa
print(
  text.startswith('Nico'))  #devuelve boleano si es verdadero o falso el inicio
print(
  text.endswith('Java'))  #devuelve boleano si es verdadero o falso el final
print(text.replace('Nico', 'Lina'))
print(text.capitalize())  #vuelve el primer caractre mayúscula de la strting
print(text.title()
      )  #vuelve la primera letra de cada palabra de la string en mayúscula
print(
  '123'.isdigit())  #devuelve un booleano indicando si o no un dígito numerico.
