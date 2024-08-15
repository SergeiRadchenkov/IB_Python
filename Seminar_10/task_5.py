'''
Вам нужно расследовать попытки несанкционированного доступа при создании каталогов для хранения 
материалов заявок-заказов (Error handling and logging) – создать Log-файл
'''
import os
import logging
import datetime

logging.basicConfig(level=logging.DEBUG, filename='test_log.log', filemode='w', encoding='utf-8')

input_path = input('Catalogue path: ')
spec_symbols = ['*', '?', '<', '>', '|', '&']
check = [characters in input_path for characters in spec_symbols]
while True in check:
    for i in range(len(check)):
        check[i] = False
    logging.info(f'{datetime.datetime.now()} Suspicious value: {input_path}')
    print('Incorrect catalogue path')
    input_path = input('Catalogue path: ')
    check = [characters in input_path for characters in spec_symbols]
command = f'mkdir {input_path}'
os.popen(command)
print('Catalogue was successfully created')
