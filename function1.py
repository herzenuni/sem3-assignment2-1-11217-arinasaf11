#Сафиуллина Арина ИВТ 2 курс
#Напишите программу, которая реализует нахождение наибольшего общего делителя двух чисел A, B
#Тесты оформите с помощью pytest или UnitTest.

def nod(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input('a = '))
b = int(input('b = '))
print ('NOD = ', nod(a, b))
