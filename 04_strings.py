name = "Nicolas"
last_name = "Posada"
age = 36
print(name)
print(last_name)

#Concatenación de srtings, como si fueera una suma.
full_name = name + " " + last_name
print(full_name)

quote = "I'm Nicolás"  #cuando se usa el apostrofe, debemos usar doble comillas para la cadena string.
print(quote)

#En el caso queramos usar el quote en una ffrase de un strings, alternamos entre comillas dobles y sencillas.
quote2 = 'She said "Hello buddy!"'
print(quote2)

#format es una forma de darle formato a los textos
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2 ', template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3 ', template3)

template4 = f"Hola, mi nombre es {name}, mi apellido es {last_name} y mi edad es {age}"
print('v3 ', template4)