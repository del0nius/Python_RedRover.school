# Домашнее задание 1:
# 1.1
# 1) Установите Python и PyCharm
# 2) Напишите и запустите программу. которая выводит строку  "Hello world!"
print("Hello world!")
# 3) Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name 
# и выводит строку  "Hello {user_name}!"
user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)
# 4) Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую операцию
# (на ваше усмотрение), и выводит “Результат = {результат}”.
x, y = input("Enter two int values separated with 'Space' key to find their sum. Input example: '1 2' ").split()
result = int(x) + int(y)
print('Результат = '+ str(result))

# 1.2
# 1) Напишите программу, чтобы вывести:
# *********
# *       *
# *       *
# *********
print('*********')
print('*       *')
print('*       *')
print('*********')