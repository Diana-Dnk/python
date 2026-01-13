# 1. Дан словарь товаров {"apple": 120, "banana": 80, "orange": 150}. 
# Вывести название товара с минимальной ценой.
# product={
#     "apple": 120, 
#     "banana": 80, 
#     "orange": 150
#     }
# min=min(product,key=product.get)
# print(min,product[min])

# 2. Дан словарь студентов {"Dias": 78, "Madina": 92, "Aruzhan": 85}. 
# Вывести всех студентов, у которых балл больше 80.
# students={
#     "Dias": 78, 
#     "Madina": 92,
#     "Aruzhan": 85
#     }
# for name,score in students.items():
#     if score>=80:
#         print(name)

# 3. Дан словарь {1: "a", 2: "b", 3: "c"}. 
# Создать новый словарь, где ключи и значения поменяны местами.
# nums = {
#     1: "a", 
#     2: "b", 
#     3: "c"
#     }
# new_nums = {}  
# for key, value in nums.items():
#     new_nums[value] = key
# print(new_nums)

# 4. Дан словарь пользователя {"name": "Dias", "age": 17}.
#  Если ключ "premium" отсутствует — добавить его со значением False.
# user= {
#     "name": "Dias", 
#     "age": 17
#     }
# if "premium" not in user:
#     user["premium"]=False
# print(user)

# 5. Дан словарь {"a": 1, "b": 2, "c": 3}. 
# Подсчитать количество ключей без использования len().
# d={
#     "a": 1, 
#     "b": 2, 
#     "c": 3
#    }
# total=0
# for key in d:
#     total+=1
# print(total)

# 6. Дан словарь товара {"apple": 5, "banana": 0, "orange": 3}. 
# Уменьшить количество каждого товара на 1, если оно больше нуля.
# list={"apple": 5, 
#       "banana": 0, 
#       "orange": 3}
# for product,price in list.items():
#     if price>0:
#         new=price-1
#         print(product,"-",new)

# 7. Дан словарь координат {"x": 10, "y": 20, "z": -5}. 
# Увеличить каждую координату в 2 раза.
# list={"x": 10, 
#       "y": 20, 
#       "z": -5}
# for cr,nums in list.items():
#     new=nums*2
#     print(cr,"-",new)

# 8. Дан словарь оценок ученика {"math": 90, "python": 100, "english": 85}. 
# Вывести среднее арифметическое.
# students = {
#     "math": 90,
#     "python": 100,
#     "english": 85
# }
# total = 0
# count = 0
# for score in students.values():
#     total += score
#     count += 1
# avg = total / count
# print(avg)

# 9. Дан список слов ["apple", "banana", "apple", "orange"]. 
# Создать словарь, где ключ — слово, значение — количество повторений.
# words = ["apple", "banana", "apple", "orange"]
# count_dict = {}  
# for word in words:
#     if word in count_dict:
#         count_dict[word] += 1
#     else:
#         count_dict[word] = 1
# print(count_dict)

# 10. Дан словарь пользователей: {1: {"name": "Dias", "role": "admin"}, 
# 2: {"name": "Arman", "role": "user"}}. Вывести только имена пользователей с ролью admin
# list={
#     1: {"name": "Dias", "role": "admin"}, 
#     2: {"name": "Arman", "role": "user"}
#     }
# for key,a in list.items():
#     if a["role"]=="admin":
#         print(a["name"])