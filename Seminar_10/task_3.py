'''
Вам нужно сделать валидацию входных данных (Input validation) для блока с выполнением 
произвольного кода
'''
import os

compute_user_input = input('\nFactors and operator for computing: ')
if not compute_user_input:
    print('No input')
else:
    print('Result: ', eval(compute_user_input, {'__builtins__':{}}))
