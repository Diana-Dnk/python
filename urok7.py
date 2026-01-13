# #вложенные циклы
# for i in range(5):
#     print(i)

# range(stop)
# range(start,stop)
# range(start,stop,step)

#Вложенный цикл - это цикл внутри другого цикла, внешний цикл отвечает за строки, а внутренний за символы внутри строки 

# for i in range(2):
#     for j in range(3):
#         print("i=", i, "j=", j)


# for i in range(1,6):
#     for j in range(1,6):
#         print("i=", i, "j=", j)


# rows=3
# cols=5
# for i in range(rows):
#     for j in range(cols):
#         print("*",end=" ")
#     print()


# rows=int(input("Введите количество строк: "))
# cols=int(input("Введите количество столбцов: "))
# for i in range(rows):
#     for j in range(cols):
#         print("#",end="")
#     print()
    

# height=int(input("Введите высоту треугольника: "))
# for i in range(1,height+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# height=int(input("Введите высоту треугольника: "))
# for i in range(height,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


# n=int(input("Введите размер квадрата: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end="")
#         else:
#             if j==0 or j==n-1:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     print()
    


# 1. Количество символов в строке (через цикл)
# Пользователь вводит слово.
# Вывести, сколько символов в слове, не используя len(), а используя цикл.

# word=input("Введите слово: ")
# a=0
# for i in word:
#     a+=1
# print(a)

# 2. Подсчитать сумму всех чётных чисел от 1 до N
# Пользователь вводит число N.
# С помощью цикла найти сумму всех чётных чисел от 1 до N включительно.
# print("Подсчитать сумму всех чётных чисел от 1 до N")
# n=int(input("Введите N число: "))
# total=0
# for i in range(1,n):
#     if i%2==0:
#         total+=i
# print(total)

# 3. Напечатать строку N раз
# Пользователь вводит фразу и число N.
# Вывести эту фразу на экран N раз, используя цикл.

# word=input("Фраза: ")
# n=int(input("Количество раз: "))
# for i in range(n):
#     print(word)

# 4. Вывести квадрат чисел
# Пользователь вводит число N.
# Вывести таблицу:
# 1 → 1
# 2 → 4
# 3 → 9
# 4 → 16
# ...
# То есть каждое число и его квадрат.

# n=int(input("n: "))
# for i in range(1,n):
#     print(i,"->",i*i)

# 5. Нарисовать квадрат из символов
# Пользователь вводит число N.
# Нарисовать квадрат N x N из символа @.
# Пример для N = 4:
# @@@@
# @@@@
# @@@@
# @@@@

# rows=int(input("Введите число: "))
# for i in range(rows):
#     for j in range(rows):
#         print("@",end="")
#     print()


# 6. Нарисовать треугольник справа
# Пользователь вводит N.
# Нарисовать правосторонний треугольник:
# Для N = 5:
#     *
#    **
#   ***
#  ****
# *****

# n=int(input("Введите высоту треугольника: "))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# 7. Найти количество цифр в числе
# Пользователь вводит целое число (например: 38291).
# Нужно посчитать, сколько в нём цифр, не используя строки.
# Работа через цикл и деление:
# 38291 → 5 цифр
# number=int(input("Ввести число: "))
# if(number==0):
#     print(1)
# else:
#     count=0
#     n=abs(number)
#     while number>0:
#         number//=10
#         count+=1
#     print("Количество цифр", count)
 
# 8. Нарисовать “лесенку чисел”
# Пользователь вводит N.
# Нужно вывести такую фигуру:
# Для N = 5:
# 1
# 12
# 123
# 1234
# 12345
# n=int(input("Ввести n: "))
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

