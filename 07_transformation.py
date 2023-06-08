#usando la misma variable como diferente tipo de datos.

name = 'Nicolas'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

#la operación de concatenación y suma debe hacerse entre variables del mismo tipo, o tendremos un error de syntax por tipos. Para eso, cuando son diferentes debemos asegurarnos de cambiar de tipo como vemos abajo usando la función del tipo de dato, eg: STR. O usanod la función format con la f""

age = 12
#forma  1: con cambiador de tipo.
print("Mi edad es " + str(age))

#forma 2: con función format.
print(f"Mi edad es {age}")

#luego aprendemos que podemos haceer conversiones directament en un input anteponiendo y luegeo usandolo como un int operando en un formato.

age2 = int(input("¿Cuál es tu edad?"))
print(f"Tu edad en 10 años será {age2 + 10}")