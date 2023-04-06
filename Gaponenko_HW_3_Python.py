# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

# # 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# - получите сумму всех чисел,
print(sum(filter(lambda i: isinstance(i, int), list_1)))
# - распечатайте все строки, где есть буква 'a'
for item in list_1:
    if isinstance(item, str) and 'a' in item:
        print(item)

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list2 = ['cat', 'dog', 'horse', 'cow']
print(tuple(list2))

# 3.4. Напишите программу, которая определяет, какая семья больше. 
# 1) Программа имеет два input() - например, family_1, family_2. 
# 2) Членов семьи нужно перечислить через запятую. 
# Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family_1 = (input("Enter family_1 members separated by comma ',' ")).split(',')
family_2 = (input("Enter family_2 members separated by comma ',' ")).split(',')
if len(family_1) > len(family_2):
    print(*family_1)
elif len(family_2) > len(family_1):
    print(*family_2)
else:
    print('Equal')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. 
# В значения можете передать информацию о вашем любимом фильме. 
film = {
    'title': 'Moneyball',
    'director': 'Bennett Miller',
    'year': 2011,
    'budget': '$50 million',
    'main_actor': 'Brad Pitt',
    'slogan': 'What are you really worth?',
}
# - распечатайте только ключи
print(film.keys())
# - распечатайте только значения
print(film.values())
# - распечатайте пары ключ - значение
print(film)

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
list = [1, 2, 3, 4, 5, 3, 2, 1]
print(set(list))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# - найдите значения, которые встречаются в обоих множествах
print(set2.intersection(set1))
# - найдите значения, которые не встречаются в обоих множествах
print(set1.symmetric_difference(set2))
# - проверьте являются ли эти множества подмножествами друг друга
print(set1.issubset(set2))
print(set2.issubset(set1))