# # class User:
# #     def __init__(self, name):
# #         self.name=name
    
# class student: 
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def is_pass(self):
#         return self.score>=50
#     def add_bonus(self,points):
#         self.score+=points
#         if self.score>100:
#             self.score=100

# s1=student("Di",49)
# s2=student("Ayan",60)
# print(s1.is_pass())
# s1.add_bonus(10)
# print(s1.score)
# print(s1.is_pass())

# class transport:
#     def __init__(self,model,speed,size):
#         self.model=model
#         self.speed=speed
#         self.size=size
#     def is_move(self):
#         print("Я еду")
#     def is_swim(self):
#         print("Я плыву")

# car=transport("BMW",290,2)
# car.is_move()

# bike=transport("Yamaha",450,1)
# bike.is_move()




# 22/01/2026
# Задание 1. Класс Person — базовая модель человека
# Условие:
# Создать класс Person.
# Атрибуты:
# name
# age
# Методы:
# greet() — выводит приветствие с именем
# is_adult() — возвращает true/false в зависимости от возраста
# birthday() — увеличивает возраст на 1
# Требования:
# Создать 2 объекта
# Вызвать все методы
# Проверить изменение состояния объекта
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(f"Привет! Меня зовут {self.name}, мне {self.age}")
#     def is_adult(self):
#         if self.age>=18:
#             print (True)
#         else:
#             print (False)
#     def birthday(self):
#         new_age=self.age+1
#         print (new_age)
# p1=Person("Di",22)
# p1.greet() 
# p1.is_adult()
# p1.birthday()

# p2=Person("Anna",16)
# p2.greet() 
# p2.is_adult()
# p2.birthday()


# Задание 2. Класс Student — работа с внутренним состоянием
# Условие:
# Создать класс Student.
# Атрибуты:
# name
# grades (массив чисел)
# Методы:
# add_grade(grade) — добавляет оценку
# get_average() — возвращает средний балл
# print_info() — выводит имя и средний балл
# Требования:
# Использовать массив
# Проверить работу методов на нескольких оценках

# class Student:
#     def __init__(self,name,grades):
#         self.name=name
#         self.grades=grades

#     def add_grade(self,grade:int):
#         self.grades.append(grade)

#     def get_average(self) -> float:
#         return sum(self.grades)/len(self.grades)

#     def print_info(self):
#         print(self.name,":",self.get_average())

# s1=Student("Di",[100,20,30])
# s1.add_grade(90)
# s1.print_info()

# второй вариант
# class Student:
#     def __init__(self,name,):
#         self.name=name
#         self.grades=[]

#     def add_grade(self,grade):
#         self.grades.append(grade)

#     def get_average(self):
#         return sum(self.grades)/len(self.grades)
    
#     def print_info(self):
#         print(self.name,"avg:",self.get_average())

# s=Student("Di")
# s.add_grade(90)
# s.add_grade(80)
# s.add_grade(100)
# s.print_info()


# Задание 3. Класс Car — логика поведения
# Условие:
# Создать класс Car.
# Атрибуты:
# brand
# speed (начальное значение 0)
# Методы:
# accelerate(value) — увеличивает скорость
# brake(value) — уменьшает скорость (не ниже 0)
# get_speed() — возвращает текущую скорость
# Требования:
# Запретить отрицательную скорость
# Проверить поведение при нескольких вызовах
# class Car:
#     def __init__(self,brand):
#         self.brand=brand
#         self.speed=0
#     def accelerate(self,value):
#         self.speed+=value

#     def  brake(self,value):
#         self.speed-=value
#         if self.speed<0:
#             self.speed=0
        
#     def get_speed(self):
#         return self.speed
    
# car=Car("Toyota")
# car.accelerate(50)
# car.brake(20)
# print(car.get_speed())


# Задание 4. Класс BankAccount — управление доступом
# Условие:
# Создать класс BankAccount.
# Атрибуты:
# owner
# balance
# Методы:
# deposit(amount)
# withdraw(amount)
# get_balance()
# Логика:
# Нельзя снять больше, чем есть
# Нельзя вносить или снимать отрицательные значения
# Требования:
# Проверить защиту от некорректных операций
# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount    
#     def get_balance(self):
#         return self.balance
    
# kaspi= BankAccount("Qwerty",1000)
# kaspi.deposit(500)
# kaspi.withdraw(200)
# kaspi.withdraw(5000)
# print(kaspi.get_balance())


# Задание 5. Класс User — работа с состоянием (login / logout)
# Условие:
# Создать класс User.
# Атрибуты:
# username
# is_logged_in (по умолчанию false)
# Методы:
# login()
# logout()
# get_status()
# Логика:
# Нельзя залогиниться дважды
# Нельзя выйти, если не залогинен

# class User:
#     def __init__(self,username):
#         self.username=username
#         self.is_auth=False

#     def login(self):
#         self.auth=True

#     def logout(self):
#         self.auth=False

#     def get_status(self):
#         if self.auth:
#             return("Online")
#         return("offline")

# u1=User("Di")
# u1.login()
# u1.logout()
# print(u1.get_status())



# Задание 6. Класс Product — вычисления внутри класса
# Условие:
# Создать класс Product.
# Атрибуты:
# name
# price
# quantity
# Методы:
# get_total_price() — price * quantity
# increase_quantity(value)
# decrease_quantity(value) (не ниже 0)
# Требования:
# Все вычисления должны быть внутри класса
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#     def get_total_price(self):
#         total = self.price*self.quantity
#         return total
    
#     def increase_quantity(self,value):
#         self.quantity += value

#     def decrease_quantity(self,value):
#         self.quantity -= value

# p1=Product("apple",100,2)
# print(p1.get_total_price())
# p1.increase_quantity(5)
# p1.decrease_quantity(2)
# print(p1.get_total_price())
     

# Задание 7. Класс Library — взаимодействие объектов
# Условие:
# Создать класс Library.
# Атрибуты:
# books (массив строк)
# Методы:
# add_book(title)
# remove_book(title)
# list_books()
# Логика:
# Нельзя удалить книгу, которой нет
# Выводить список книг в читаемом виде

    
