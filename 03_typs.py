# Strings: cadena de caracteres (texto)
my_name = "Nicolás"
my_name1 = "Lina"
# texto entre comillas es para constantes en el valor impreso.
intro = 'My name is ' + my_name + ', and my wife name is ' + my_name1
print(intro)
print(type(my_name))

# integer, o números enteros.
my_age = 36
print(intro, 'and my age is', my_age)
print(type(my_age))

# booleanos, valos verdaderos o falsos.
is_single = False
print('Es soltero? ', is_single)
print(type(is_single))

# input da valorse a las variables
my_age = input('Cuál es tu edad?')
print('Mi edad es ', my_age)
print(type(my_age))