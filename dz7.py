# 1. Нарисовать прямоугольник N x M из символа '@'
# a=2
# b=3
# for i in range(a):
#     for j in range(b):
#         print("@",end=" ")
#     print()

# 2. Вывести треугольник высотой N (левая версия):
# *
# **
# ***
# for i in range(1,3+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# 3. Вывести перевёрнутый треугольник высотой N.
# n=int(input("Введите высоту N: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# 4. Построить таблицу умножения от 1 до N.
# n=int(input("Введите число N: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j,end="\t" )
#     print()

# 5. Нарисовать квадрат N x N, где рамка состоит из '*', а внутри пробелы.
# n=int(input("Введите размер квадрата N: "))
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

# 6. Нарисовать квадрат с двумя диагоналями.
# n=int(input("Введите размер квадрата N: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j == 0 or j == n-1:
#              print("*",end="")
#         elif i == j:
#             print("*", end="") 
#         elif i + j == n - 1:
#             print("*", end="")
        
#         else:
#             print(" ", end="")
#     print()   

# 7. Построить числовую лестницу:
# 1
# 12
# 123
# 1234
# n=int(input("Введите число N: "))
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#8. Построить правосторонний треугольник (с пробелами слева).
# n=int(input("Введите высоту треугольника: "))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

#9. Сгенерировать квадрат чисел от 1 до N*N.
# n = int(input("Введите N: "))
# num = 1
# for i in range(n):
#     for j in range(n):
#         print(num, end=" ")
#         num += 1
#     print()

# 10. Построить шахматную доску из '*' и пробелов.
# a=10
# b=10
# for i in range(a):
#     for j in range(b):
#         if (i+j)%2==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()