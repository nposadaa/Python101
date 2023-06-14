x = 3.3
print('x =', x)

y = 1.1 + 2.2
print('y =', y)

print('Is x = y?', x == y)

y_str = format(y, ".2g")
print('\n', '*' * 10)
print('\n', 'This is a String solution to float comparison problem', '\n',
      'y convertd to str =>', y_str)
print('Is x str = y str?:', y_str == str(x))

print('\n', '*' * 10)

tolerance = 0.00001
#abs nos retorna el valor absoluto de una operación, es decir el positivo.
diff_abs = abs(x - y)
print('Value of absolute difference:', diff_abs)
print('\n', 'This is a math solution to float comparison problem',
      'Is diffence between them smaller than tolerance:', diff_abs < tolerance)
