'''
Напишите программу на Python, которая будет проверять вводимый пользователем 
пароль на сложность (Authentication and password management):
● не менее 8 символов
● наличие прописных и строчных букв
● наличие цифр
● и переводит его в хэш-значение
'''
import hashlib


def check_password():
    pswrd = input('Пожалуйста, введите пароль: ')
    while True:
        if len(pswrd) < 8:
            print(f'Вы ввели пароль меньше 8')
            pswrd = input('Пожалуйста, введите пароль: ')
        cnt_upper = sum(1 for i in pswrd if i.isupper())
        cnt_lower = sum(1 for i in pswrd if i.islower())
        cnt_digit = sum(1 for i in pswrd if i.isdigit())
        if cnt_upper == 0:
            print('В вашем коде нет заглавных букв')
            pswrd = input('Пожалуйста, введите пароль: ')
        elif cnt_lower == 0:
            print('В вашем коде нет прописных букв')
            pswrd = input('Пожалуйста, введите пароль: ')
        elif cnt_digit == 0:
            print('В вашем коде нет цифр')
            pswrd = input('Пожалуйста, введите пароль: ')
        else:
            good_pswrd = hashlib.sha256(pswrd.encode()).hexdigest()
            print(f'Вы ввели надёжный пароль.\nХэш пароля: {good_pswrd}')
            break


if __name__ == '__main__':
    check_password()
