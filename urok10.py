#list[]
#tuple()

#повторение
# nums=[10,20,30,40,50]
# mix=[10,20,True,"qwerty",3.14]
# names=["Diana","Dias","Mansur"]
# print(nums[0])

# nums=[10,20,30,40,50]
# nums[0]="qwerty"
# nums.append(40)
# nums.insert(4,40)
# print(nums)

# Задача 1 (разогрев
# )Дан список nums = [5, 2, 9, 1, 7
# ]Выведите первый и последний элемент
# ыОтсортируйте список по возрастани
# юВыведите длину списка

# nums = [5, 2, 9, 1, 7]
# print(nums[0])
# print(nums[4])
# nums.sort()
# len_nums=len(nums)
# print(nums)
# print(len_nums)

# Дан список a = [10, 20, 30, 40]
# Замените второй элемент на 999, добавьте в конец число 111 и удалите первый элемент.
# a = [10, 20, 30, 40]
# a[1]=999
# print(a)
# a.append(111)
# print(a)
# a.remove(10)
# print(a)

# Пользователь вводит 5 чисел (по одному).
# Сохраните их в список и выведите сумму.
# list=[]
# for i in range(5):
#     num=int(input("Введите число: "))
#     list.append(num)
# print(list)
# print(sum(list))


# Дан список оценок:
# grades = [50, 90, 75, 100, 60, 88]
# Найти максимальную оценку
# Посчитать среднюю
# # Сколько оценок ≥ 80?

# grades = [50, 90, 75, 100, 60, 88]
# print(max(grades))
# print(sum(grades)/len(grades))
# count_good=0
# for i in grades:
#     if i>=80:
#         count_good+=1
# print(count_good)


#для списка заказов [ID,цена]: найдите сумму, минимальную цену и ее ID
# orders=[
#     [301,990],
#     [302,12000],
#     [303,2000],
#     [304,10000],
#     [305,5000],
# ]
# total=0
# for i in orders: 
#     total+=i[1]
# min_price=orders[0][1]
# min_id=orders[0][0]
# for i in orders:
#     order_id=i[0]
#     price=i[1]
# if price<min_price:
#     min_price=price
#     min_id=order_id
# print(total)
# print(min_price)
# print(min_id)



# tuple - картежи
# numbers = (10, 20, 30)
# print(numbers[0])


#tuple
# nums=(10,20,30)
# print(nums[0])

#индексы и срезы одинаковые 
# t=(10,20,30,40,50)
# print(t[0])
# print(t[-1])
# print(t[1:3])

# ------------------------строки-------------------------

# a="qwerty"
# for i in a:
#     print(i)

# text="python"
# print(text[0])
# print(text[-1])
# print(len(text))

# text="python"
# print(text[0:2])
# print(text[2:5])
# print(text[:3])
# print(text[3:])
# print(text[::-1])

#Методы изменения регистра 
# name="DIas"
# print(name.lower())
# print(name.upper())
# print("hello world".title())
# print(name.capitalize())

# name=input("Введите имя: ")
# clean_name=name.strip().lower().capitalize()
# print("Привет",clean_name)

# replace замена текста
# text="i like JS. JS is cool"
# new_text=text.replace("JS","python")
# print(new_text)

# text="hello world everthing is good"
# print(text.replace(" ","_"))

# text="hello world everthing is good"
# words=text.split()
# print(words)
# print(len(words))

# data="Dias,18,95"
# parts=data.split(",")
# print(parts)

# words=["i","hate","C++"]
# words2=" ".join(words)
# print(words2)

# in find()
# text="hello world everthing is good"
# print("world" in text)
# print("cat" in text)
# print(text.find("world"))
# print(text.find("cat"))

# 1.Пользователь вводит своё имя.
# Выведите Привет, <Имя>!, где имя приведено к нормальному виду (первая буква заглавная, лишние пробелы убраны).
# name=input("Введите имя: ")
# print("привет",name.capitalize().strip())

# 2.Пользователь вводит строку.
# Выведите:
# количество символов
# количество пробелов
# word=input("Введите строку: ")
# spaces=0
# for i in word:
#     if i==" ":
#         spaces+=1
# print(spaces)
# len_word=len(word)
# print(len_word)


# 3.Пользователь вводит предложение.
# Выведите количество слов.
# text=input("Введите предложение: ")
# word=text.split()
# print(word)
# print(len(word))

# 4.Пользователь вводит строку.
# Сделайте так, чтобы:
# все буквы были маленькими
# все пробелы заменены на _
# word=input("Введите строку: ")
# word_new=word.lower().replace(" ","_")
# print(word_new)

# 5.Пользователь вводит слово.
# Посчитайте, сколько в нём гласных букв (а, о, е, ё, и, ы, у, ю, я).
# word=input("Введите строку: ")
# Total=0
# for i in word:
#     if i=="а" or i=="о" or i=="е" or i=="ё":
#         Total+=1
# print(Total)        


# word=input("Введите строку: ")
# a="аоеёиыуюя"
# Total=0
# for i in word:
#      if i in a:
#         Total+=1
# print(Total) 