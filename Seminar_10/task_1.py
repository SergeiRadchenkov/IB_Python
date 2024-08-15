'''
Вам нужно сделать валидацию входных 
данных (Input validation) для умножения 
данных в заявке-заказе
'''
x = input('1st factor <= 10 digit number: ')
y = input('2nd factor <= 10 digit number: ')
while (len(x) > 10 or (not x.isdigit())) or (len(y) > 10 or (not y.isdigit())):
    print('There is no 10 digit number: ')
    x = input('1st factor <= 10 digit number:')
    y = input('2nd factor <= 10 digit number:')
x = int(x)
y = int(y)
print('Total = ', x*y)
