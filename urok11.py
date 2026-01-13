# lower() -> строчные буквы
# upper() -> КАПСЛОК
# capitalize() -> Нормальный вид текста
# strip() -> убирает пробелы
# lstrip() ->
# rstrip() ->
# find() -> находит элемент, пишет индекс
# title() -> нормальный вид текста как в предложения
# join() -> из массива в текст
# split() -> из текста в массив
# replace() -> Заменяем значение на нужное (Что менять, На что хотим поменять)

#Список хранит просто значение 
#словарь хранит информацию объекта
# student={
#     "name":"Dias",
#     "age":18,
#     "city":"Astana",
#     "isStudent": True
# }
# student["grade"]=90
# student["age"]=17
# print(student["name"])
# student.pop("age")
# # print(student["age"])
# print(student.get("grade","нет оценеки"))
# get -> безопасный способ получения данных


# student={
#     "name":"Dias",
#     "age":18,
#     "city":"Astana",
#     "isStudent": True
# }
# for i in student:
#     print(i)

# for i in student.values():
#     print(i)

# for key,value in student.items():
#     print(key, "-", value)


# user = {
#     "name":"Dias",
#     "age":18,
#     "scores":{
#         "math":90,
#         "py":100
#     }
# }
# print(user["scores"]["py"])

# #1
# studens={
#     "Dias":100,
#     "Madina": 95,
#     "Aruzhan":60
# }
# for name,score in studens.items():
#     print(name,":",score)
# # #2
# best=max(studens,key=studens.get)
# print(best,studens[best])

# pairs=[
#     ("Aruzhan",16),
#     ("Dias",17)
# ]
# d=dict(pairs)
# print(d)

# users= {
#     1:{"name":"Dias","role":"admin"},
#     2:{"name":"ALmas","role":"user"}
# }
# for user_id, info in users.items(): #все сразу 
#     print(f"ID: {user_id}, Name:{info["name"]}, Role:{info["role"]}")
# for i in users: #только ключи
#     print(i)
# for i in users.values(): #только значения
#     print(i)


# 1. Создайте словарь с именем и возрастом. Выведите возраст.
# # Пример:
# {"name": "Aruzhan", "age": 17}
# students={
#     "name":"Aruzhan",
#     "age":17
# }
# print(students["age"])

# 2. Дан словарь. Измените значение ключа "age" на новое число.
# student={
#     "name":"Aruzhan",
#     "age":17,
#     "city":"Almaty"
# }
# student["age"]=18
# print(student)

# 3. Добавьте в словарь новый ключ "city" со значением.
# students={
#     "name":"Aruzhan",
#     "age":17
# }
# students["city"]="Almaty"
# print(students)

# 4. Удалите из словаря ключ "age".
# student={
#     "name":"Aruzhan",
#     "age":17,
#     "city":"Almaty"
# }
# student.pop("age")
# print(student)

# 5. Дан словарь из трёх предметов и баллов. Выведите все ключи и все значения.
# list={
#     "math":90,
#     "py":84,
#     "JS":78
# }
# for name,score in list.items():
#     print(name,"-",score)
# 6. Дан словарь из товаров: название → цена. Найдите самую дешёвую цену.
# list={
#     "яблоко":100,
#     "молоко":400,
#     "хлеб":300
# }
# min=min(list,key=list.get)
# print(min,list[min])
    
# **7. Создайте словарь студентов: имя → балл.
# Выведите только тех, у кого балл ≥ 80.**
# students={
#     "Dias":89,
#     "Diana":90,
#     "Sofia":67,
#     "Nastya":56
# }
# for name,score in students.items():
#     if score>=80:
#         print(name,"-",score)


# **8. Дан словарь {1: "a", 2: "b", 3: "c"}.
# Поменяйте местами ключи и значения.**
# list={
#     1: "a", 
#     2: "b", 
#     3: "c"
# }
# swapped={value:key for key,value in list.items()}
# print(swapped)
# for key,name in list.items():
#     print(name,"-",key)


# **9. Дан словарь пользователя.
# Если ключ "premium" отсутствует — добавьте его со значением False.**
# user={
#     "name":"Dias",
#     "age":17
# }
# if "premium" not in user:
#     user["premium"]=False
# print(user)


# 10. Подсчитайте количество ключей в словаре без функции len().
# list={
#     "cola":2,
#     "milk":1,
#     "apple":5,
# }
# total_key=0
# for key in list:
#     total_key+=1
# print(total_key)

# **11. Дан словарь: товар → количество.
# Уменьшите количество товара на 1, если оно больше нуля.**
# list={
#     "cola":2,
#     "milk":1,
#     "apple":5,
# }
# for product,col in list.items():
#     if col>0:
#         a=col-1
#         print(product,"-",a)

# **12. Дан словарь с координатами точки:
# {"x": 10, "y": 20, "z": -5}
# Увеличьте каждую координату в 2 раза.**
# nums={
#     "x": 10, 
#     "y": 20, 
#     "z": -5
# }
# for coor,value in nums.items():
#     a=value*2
#     print(coor,"-",a)

# **13. Дан словарь учащихся: имя → список оценок.
# Найдите средний балл каждого ученика.**
# Пример:
# {"Dias": [90, 80], "Madina": [100, 95]}
# studens={
#     "Dias": [90, 80], 
#     "Madina": [100, 95]
#     }
# for name,value in studens.items():
#     value_s=sum(value)/len(value)
#     print(name,"-",value_s)

# 14. Дан список слов. Подсчитайте частоту каждого слова с помощью словаря.
# Пример:
# ["apple", "banana", "apple"] → {"apple": 2, "banana": 1}
# Words=["apple","banana","melon","apple","apple","apple"]
# dict2={}
# for i in Words:
#     dict2[i]=dict2.get(i,0)+1
# print(dict2)

# 15. Дан текст. Используя словарь, посчитайте частоту каждого символа.
# text = "hello world"
# dict3={}
# for i in text:
#     dict3[i]=dict3.get(i,0)+1
# print(dict3)

# **16. Дан словарь пользователей: id → данные.
# Выведите имена всех пользователей с ролью “admin”.**
# list={
#     "Dias":"user",
#     "Diana":"admin",
#     "Sofia":"user",
#     "Valera":"admin"
# }
# for name,key in list.items():
#     if key=="admin":
#         print(name,"-",key)

# **17. Дан словарь: категория → список товаров.
# Посчитайте общее количество всех товаров во всех категориях.**
# Пример:
# {"fruits": ["apple", "banana"], "cars": ["bmw"]} → 3
# list={
#     "fruits": ["apple", "banana"],
#     "cars": ["bmw"],
# }
# total=0
# for i in list.values():
#     total+=len(i)
# print(total)

# **18. Дан список словарей (каждый словарь — ученик).
# Найдите ученика с максимальным средним баллом.**
# Пример:
# [
#   {"name": "Dias", "scores": [80, 90, 100]},
#   {"name": "Madina", "scores": [95, 90, 88]}
# ]
# studens= [
#   {"name": "Dias", "scores": [80, 90, 100]},
#   {"name": "Madina", "scores": [95, 90, 88]}
# ]




# **19. Дан словарь магазина: товар → {цена, количество}.

# Найти товар с максимальной стоимостью цена × количество.**

# **20. Дан словарь-задания: студент → {completed, total}.

# Для каждого студента посчитайте процент выполнения.
# Найдите того, у кого процент самый высокий.**

# Пример:

# {
#   "Dias": {"completed": 7, "total": 10},
#   "Madina": {"completed": 9, "total": 12}
# }