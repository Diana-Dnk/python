# # 1. Нарисовать прямоугольник N x M из символа '@'.
# a=5
# b=10
# for i in range(a):
#     for j in range(b):
#         print("@", end="")
#     print()

# 2. Вывести треугольник высотой N (левая версия):
# *
# **
# ***
# a=3
# for i in range(1,a+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# 3. Вывести перевёрнутый треугольник высотой N.
# n=int(input("Введите высоту N: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# 4. Построить таблицу умножения от 1 до N.
# n=int(input("Введите чтсло N: "))
# for i in range(1,n+1):
#     for j in range (1,n+1):
#         print(i*j, end="\t")
#     print()


# 5. Нарисовать квадрат N x N, где рамка состоит из '*', а внутри пробелы.
# n=int(input("Введите размер квадрата N: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end="")
#         else:
#             if j==0 or j==n-1:
#                  print("*",end="")
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
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#8. Построить правосторонний треугольник (с пробелами слева).
# n=int(input("Введите высоту треугольника: "))
# for i in range(1,n+1):
#     for space in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#             print("*", end="")
#     print()

#  10. Построить шахматную доску из '*' и пробелов.
# a=10
# for i in range(a):
#     for j in range(a):
#         if (j+i)%2==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()