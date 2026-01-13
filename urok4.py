# time = int(input("Введите время: "))%24
# ticket = True
# money =False
# luggage=True
# print((ticket or money) and  not luggage and time>6)

# number=int(input("Введите ваш возраст: "))
# status="adult" if number>=18 else "child"
# print(status)

# odd=number if number%2==0 else 0
# print(odd)

# print(ord("a"))
# print(chr(97))

# name="Diana"
# bool_Diana=True if name=="Diana" else False 
# print(bool_Diana)


# number=156
# if number>5:
#     number+=5
# print(number)

# number=156
# if number>5:
#     number+=5
# print(number)

#Error
# number=10
# if number>15:
#     number1=10
# else:
#     number1=0
# print(number1)

# bank=int(input("Enter the bank account amount: "))
# if bank>0:
#     print("Bank amount is", bank)
#     human=int(input("enter how mach you put: "))
#     if human<=bank:
#         bank-=human
#         print("You put", human, "now yout bank amount is", bank)
#     else:
#         print("not enough money")
# else:
#     print("Invalid bank amount")

# number=int(input("Enter a number: "))
# if number>0:
#     print("Greater than 0")
#     if number>10:
#         print("Greater than 10")
#         if number>20:
#             print("Greater than 20")
#         else:
#             print("Less than or equal to 20")


# sec=int(input("Введите время в секундах, прошедшее с начала дня: "))
# chois=input("Узнать сколько часов/минут/секунд осталось до полуночи:  ")
# day=86400
# if chois=="часов":
#     print("Остаток в часах", (day-sec)/3600)
# elif chois=="минут":
#     print("Остаток в минутах", (day-sec)/60)
# elif chois=="секунд":
#     print("Остаток в секундах", day-sec)


# d=int(input("Введите диаметр окружности: "))
# chois=input("Что вы хотите найти площадь/периметр ")
# if chois=="площадь":
#     print("Площадь круга равна", (3.14*d**2)/4)
# elif chois=="периметр":
#     print("Площадь круга равна", 3.14*d)

# -m venv venv

# venv\scripts\activate

# try:
#     age=int(input("Введите число "))
# except:
#     print("Error")
# print("Hello")

# try:
#     print(5/0)
#     print("5+9")
#     age=int(input("Введите число "))
# except:
#     print("Error")
# print("Hello")


# try:
#     print("5+9")
#     age=int(input("Введите число "))
# except Exception as e:
#     print(e)
# print("Hello")


# a=int(input("Стоимость одной игровой приставки: "))
# b=int(input("Количество: "))
# с=int(input("Размер скидки: "))
# choice=input("посчитать общую сумму заказа или одну приставку со скидкой ")
# if choice=="1":
#     print("общая сумма заказа:", (a*b))
# if choice=="2":
#     print("одна приставка со скидкой:", (a*(с/100))) 

# a=(int(input("Введите кол числов: ")))
# if (0<a<=6):
#     print("Good night")
# elif(7<=a<=13):
#     print("Good morning")
# elif(14<=a<=17): 
#     print("Good afternon")