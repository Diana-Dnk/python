# text="dfffffffddstsgfvvfrea"
# sum=0
# for i in text:
#     if i=="f":
#         sum+=1
# print("Количество букв 'f'", sum)

# Total=0
# num=int(input("Введите число 0 для стопа: "))
# while num!=0:
#     Total+=num
#     num=int(input("Введите число 0 для стопа: "))
# print("Сумма: ", Total)

# secret=12
# attempt=int(input("Угадай число: "))
# while attempt!=secret:
#     print("Неверно")
#     attempt=int(input("Угадай число: "))
# print("Молодец")

# Task1
# a=1
# b=50
# total=0
# for i in range (a,b+1):
#     total+=i
# print("Общая сумма:",total)

# Task2
# a=1
# b=100
# total=0
# for i in range(a,b+1):
#     if i%2==0:
#         total+=i
# print(total)

# task3
# a=-10
# b=5
# for i in range(a,b+1):
#     if i<0:
#         print(i, end=" ")


#новая тема break/continue/pass

# word="Kaboom"
# for i in word:
#     if i=="a":
#         print("Найдена буква а")
#         break
# print("Смотрим", i)

# for i in range(0,10):
#     if i==4:
#         print("Остановка")
#         break
# print(i)

# while True:
#     num=int(input("ВВеди число (отрицательно-стоп): "))
#     if num<0:
#         print("остановка")
#         break
#     print("Ты вел", num)

# secret=5
# while True:
#     a=int(input("Угадай число: "))
#     if a==secret:
#         print("Угадал")
#         break
#     print("Не угадал")

# for i in range(1,21):
#     if i%2!=0:
#         continue
#     print("Четное", i)

# while True:
#     text=input("ВВедите текст(стоп->выход): ")
#     if text=="стоп":
#         break
#     if text=="":
#         continue
# print("Вы ввели", text)

# word="programming"
# for i in word:
#     if i not in "aeiouy":
#         continue
#     print("Гласная",i)


# for i in range(5):
#     if i == 3:
#         pass
#     print(i)



# print("------Мини касса------")
# print("Введите цену товара. 'pay' -> авершить: ")
# total=0
# while True:
#     data=input("Цена: ")
#     if data =="pay":
#         break
#     if data =="":
#         continue
#     price=float(data)
#     if price <0:
#         print("Цена не может быть меньше 0")
#         continue
#     total+=price
#     print("Текущая сумма:", total)
# print("Итог:", total)

# print("------Мини магазин------")
# print("Введите цифру: 1-добавить товар,2-показать,3-оплатить,0-выход")
# total=0
# while True:
#     data=input("Введите цифру: ")
#     if data =="0":
#         break
#     if data =="":
#         continue
#     num=float(data)
#     if num==1:
#         a=input("Добавить товар: ")
#         b=int(input("Введите цену товара: "))
#         total+=b
#         print("Товар добавлен!","Текущая сумма: ", total)
#     if num==2:
#         print("Общая сумма корзины:",total)
#     if num==3:
#         print("Оплатить покупку на сумму:", total)
# print("Спасибо за покупку")

# name=input("Введите имя: ")
# a=name 
# for i in range(5): 
#     print(a)
