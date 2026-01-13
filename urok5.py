# try:
#     print(5/0)
# except Exception as e:
#     print(e)

# try: 
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide be zero")

# try:
#     print(5/0)
# except (ZeroDivisionError, ValueError):
# except Exception as e:
#     print(e)

# try:
#     money=int(input("enter amount of money: "))
#     if money<0:
#         raise ValueError ("Money can't be negative")
# except Exception as e:
#     print(e)

# try:
#     number=int("ten")
# except (ZeroDivisionError,ValueError):
#     print("Ошибка преобразования или деления")
# except Exception as e:
#     print(e)
# finally:
#     print("Finished")

# Новая тема: циклы 
# x=0
# while x<10:
#     print("Hello") #итерация
#     x+=1

# stop_loop=True
# x=0
# while stop_loop:
#     print("infinite loop")
#     x+=1
#     if x==10:
#         stop_loop=False

# stop_loop=True
# x=0
# while True:
#     print("infinite loop")
#     x+=1
#     if x==10:
#         stop_loop=False


# a=int(input("Введите число: "))
# b=int(input("Введите второе число: "))
# sum=0
# while a<=b:
#     print(a, end=" ")
#     sum+=a
#     a+=1
# print(sum)

# word="Python"
# for i in word:
#     print(i, end=" ")

# for i in range(1,11):
#     print(i, end=" ")


# for i in range(11):
#     print(i, end=" ")


# for i in range(1,11,2):
#     print(i, end=" ")

# for i in range(1,11,2):
#     print(i*10, end=" ")

# for i in range(1000,990,-1):
#     print(i, end=" ")

#task 1
# try:
#     number=int(input("Введите шестизначное число: "))
#     if number>999999:
#         raise ValueError("Number is too big")
#     elif number<100000:
#         raise ValueError("Number is too small")
#     num1=number//100000%10
#     num2=number//10000%10
#     num3=number//1000%10
#     num4=number//100%10
#     num5=number//10%10
#     num6=number%10

#     if num1+num2+num3 == num4+num5+num6:
#         print("Lucky number")
#     else:
#         print("Not a lucky number")
# except Exception as e:
#     print(e)

#task2
# try:
#     number=int(input("Введите шестизначное число: "))
#     if number>999999:
#         raise ValueError("Number is too big")
#     elif number<100000:
#         raise ValueError("Number is too small")
    
#     num1=number//100000%10
#     num2=number//10000%10
#     num3=number//1000%10
#     num4=number//100%10
#     num5=number//10%10
#     num6=number%10

#     total_number=num1*100000+num2*10000+num3*1000+num4*100+num5*10+num6
#     print(total_number)

# except Exception as e:
#     print(e)

# try:
#     number=int(input("Введите число: "))
#     if number>12:
#         raise ValueError("Number is too big")
#     elif number<1:
#         raise ValueError("Number is too small")
#     elif number==1 or number==2 or number==12:
#         print("Winter")
#     elif number==3 or number==4 or number==5:
#         print("Spring")
#     elif number==6 or number==7 or number==8:
#         print("Summer")
#     elif number==9 or number==10 or number==11:
#         print("Autumn")
# except Exception as e:
#     print(e)



# for i in range(1,11):
#     print(i)
#     for j in range(1,6):
#         print(j)

# for i in range(1,11):
#     for j in range(1,6):
#         print(i*j, end="\t")
#     print()

# for i in range(1,11):
#     for j in range(1,6):
#         for k in range(1,11):
#             print(i,j,k)


# num1=int(input("Number: "))
# num2=int(input("Number2: "))
# for i in range (num1,num2):
#     if i%2==0:
#         print(i)

# num1=int(input("Number: "))
# num2=int(input("Number2: "))
# for i in range (num1,num2):
#     if i%2==1:
#         print(i)


# num1=int(input("Number: "))
# num2=int(input("Number2: "))
# if num1>num2:
#     for i in range (num1,num2,-1):
#         print(i)
# elif num1<num2:
#     for i in range (num2,num1,-1):
#         print(i)

#1 вариант
# a=int(input("Number: "))
# b=int(input("Number2: "))
# if a>b:
#     for i in range (b,a+1):
#         if i%2==1:
#             print(i)
# elif a<b:
#     for i in range (a,b+1):
#         if i%2==1:
#             print(i)

#2 вариант
# a=int(input("Number: "))
# b=int(input("Number2: "))
# if a>b:
#     a,b=b,a
# for i in range (a,b+1):
#     if i%2==1:
#         print(i)



