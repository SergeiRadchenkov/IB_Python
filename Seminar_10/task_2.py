'''
Вам нужно сделать валидацию входных данных (Input validation) и санитизацию выходных данных 
(Sanitize) в команды к операционной системе при создании каталогов для хранения материалов заявок-заказов
'''
import os

input_path = input('Catalogue path: ')
spec_symbols = ['*', '?', '<', '>', '|', '&']
check = [characters in input_path for characters in spec_symbols]
while True in check:
    for i in range(len(check)):
        check[i] = False
    print('Incorrect catalogue path')
    input_path = input('Catalogue path: ')
    check = [characters in input_path for characters in spec_symbols]
command = f'mkdir {input_path}'
os.popen(command)
print('Catalogue was successfully created')
