# and: 
print('''Example of how AND works by
comparing to identical variables True:''','\n')
print('True and True =>', True and True)
print('True and False =>', True and False)

print('\n','*' * 10,'\n')
print('''Example of how AND works by
comparing to identical INT variables:''','\n')
print('10 > 5 and 5 < 10 =>', 10 > 5 and 5 < 10)
print('10 < 5 and 5 > 10 =>', 10 < 5 and 5 > 10)
print('10 < 5 and 5 < 10 =>', 10 < 5 and 5 < 10)

# OR
print('\n','*' * 10,'\n')
print('''Example of how OR works by
comparing to booleans. OR will be always True as long something is true:''','\n')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('True or False =>', False or False)

print('\n','*' * 10,'\n')
print('''Example of how OR works by
using an example of users giving their role:''','\n')
role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')