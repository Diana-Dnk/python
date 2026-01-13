# создание массивов (списков)
# numbers=[10, 20, 30, 40, 50]
# names=["Dias","Aurean", "Diana", "Almat"]
# mixed=["Dias",3.12,123,True]
# empty=[]
# print(numbers,mixed,names,empty)

# индексы внутри списков 
# numbers=[10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[4])

#отрицательные индексы с конца
# numbers=[10, 20, 30, 40, 50]
# print(numbers[-1])
# print(len(numbers)-1)

#mutation-мутация(изменение)
# numbers=[10, 20, 30, 40]
# numbers[0]=100
# numbers[1]=200
# numbers[2]="qwerty"
# numbers[3]=True
# print(numbers)

#перебор массива делается через цикл for
# numbers=[10, 20, 30, 40]
# for i in numbers:
#     print(i)

#перебор массива где мы отдельно показываем индексы:
# numbers=[10, 20, 30, 40]
# for i in range(len(numbers)):
#     print("индекс:", i,"значение", numbers[i])

#слайсы
# numbers=[10, 20, 30, 40, 50]
# print(numbers[1:4]) элементы с индекса 1 до 3
# print(numbers[:3]) элементы с начала до 2 индекса 
# print(numbers[2:]) с индекса 2 до конца
# print(numbers[-2:]) последние 2 


#основные операторы с массивом 
#нахождение элемента внутри массива возращает TRUE/FALSE 
# numbers=[10, 20, 30, 40, 50]
# print(10 in numbers)
# print(60 in numbers)

#ариф операторы с массивом 
# a=[1,2]
# b=[2,3]
# w=["qwerty",True]
# c=a+b+w  #минус и деление нельзя
# print(c)

# zero=[0]*5
# print(zero)


# 1. Вывести первый и последний элемент
# Дан список чисел. Выведи первый и последний элемент через пробел.

# numbers=[10,20,30,40]
# print(numbers[0])
# print(numbers[3])
# print(numbers[-1])

# 2. Вывести элементы по индексам
# Дан список из 5 элементов. Выведи элемент с индексом 2 и элемент с индексом -2.

# numbers=[10,20,30,40]
# print(numbers[2])
# print(numbers[-2])

# 3. Изменить значения в списке
# Дан список [10, 20, 30, 40].
# Замени:
# первый элемент на 100
# последний на "END"
# Выведи результат.

# numbers=[10,20,30,40]
# numbers[0]=100
# numbers[3]="END"
# print(numbers[0], numbers[3])

# 4. Сумма элементов вручную
# Дан список чисел.
# Через цикл найди сумму всех элементов (не использовать sum()).

# numbers=[10,20,30,40]
# total=0
# for i in numbers:
#     total+=i
# print(total)

# 5. Найти максимальный элемент вручную
# Дан список.
# Через цикл найди самое большое число.

# numbers=[23,99,65,40,537,545,1,234,35,6]
# max_value=numbers[0]
# for i in numbers:
#     if i>max_value:
#         max_value=i
# print(max_value)
    
# 6. Подсчитать количество чётных чисел
# Через перебор посчитай, сколько в списке чётных элементов.

# numbers=[10,20,33,40]
# a=0
# for i in numbers:
#     if i%2==0:
#         a+=1
# print(a)

# 7. Вывести индексы и значения
# Через range(len(list)) выведи:
# Индекс: X → Значение: Y

# numbers=[10,20,33,40]
# for i in range(len(numbers)):
#     print("Индекс:",i,"значение", numbers[i])

# 8. Слайс: вывести середину
# Дан список из 7 элементов.
# Выведи средние 3 элемента через слайс.

# numbers=[10,20,30,40,50,60,70]
# print(numbers[2:5])

# 9. Проверить, есть ли число в списке
# Пользователь вводит число.
# Если оно находится в списке — вывести "YES", иначе "NO".

# numbers=[10,20,30,40,50,60,70]
# n=int(input("Введите число: "))
# if n in numbers:
#     print("yes")
# else:
#     print("no")    

# 10. Соединить два списка
# Даны два списка.
# Создай третий, который представляет собой их конкатенацию.

# numbers1=[10,20,30,40,50,60,70]
# numbers2=[56,256,3560,4560,576,70,70]
# c=numbers1+numbers2
# print(c)

# 11. Создать список из пяти нулей
# Используя умножение списков ([0] * N), создай список из 5 нулей.

# number=[0]*5
# print(number)

# 12. Увеличить каждый элемент на 10
# Не меняя оригинальный список, создай второй, где каждый элемент увеличен на 10.

# numbers=[10,20,30,40,50,60,70]
# new_massiv=[]
# for i in numbers:
#     new_massiv+=[i+10]
# print(new_massiv)

# 13. Найти количество элементов вручную
# С помощью цикла подсчитай длину списка (не использовать len()).

# numbers=[10,20,30,40,50,60,70,34]
# total=0
# for i in numbers:
#     total+=1
# print(total)

# 14. Развернуть список вручную
# Дан список.
# Создай новый список, куда элементы копируются с конца к началу.

# numbers=[10,20,30,40,50,60,70,34]
# num=[]
# for i in range(len(numbers)-1,-1,-1):
#     num+=[numbers[i]]
# print(num)

# 15. Фильтр: оставить только строки
# Дан смешанный список, например:
# ["A", 123, "Qwerty", True, "X"]

# list=["A", 123, "Qwerty", True, "X"]
# only_str=[]
# for i in list:
#     if type(i)==str:
#         only_str+=[i]
# print(only_str)
   

#Методы
# append(x)
# extend
# insert
# remove
# pop
# clear
# reverse
# sort
# copy 
#index

# append -> добавить элемент в конец
# numbers=[1,5,9]
# numbers.append(23)
# print(numbers)

# extend -> расширить список элемента другого списка
# a=[1,2,3]
# b=[4,5]
# a.extend(b)
# print(a)

# insert -> добавление элемента через  индекс 
# nums=[10,20,30]
# nums.insert(1,15)
# nums.insert(0,"❤️")
# print(nums)

# remove -> удаление элемента по значению 
# nums=[10,20,30,40]
# nums.remove(20)
# print(nums)

# pop -> удаление элемента по индексу
# nums=[10,20,30,40]
# nums.pop(2)
# print(nums)

# clear -> полность удаляет значение массива
# nums=[10,20,30,40]
# nums.clear()
# print(nums)

# reverse -> переворачивает текущие значение
# nums=[10,20,30,40]
# nums.reverse()
# print(nums)

# sort -> сортировка массива по условию
# nums=[5,2,3,1,4]
# nums.sort()
# print(nums)

# names=["Диас", "Бекжан","Алия"]
# names.sort()
# print(names)

# copy -> копирование массива либо элемент
# original=[1,2,3]
# copy_massiv=original.copy()
# copy_massiv.append(34)
# print(copy_massiv)