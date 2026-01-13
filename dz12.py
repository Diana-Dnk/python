# 1. Создать функцию hello(), которая выводит:
# Привет! Это моя первая функция
# def hello():
#     print("Привет! Это моя первая функция")
# hello()

# 2. Создать функцию greet(name), которая выводит:
# Привет, <name>
# def greet(name):
#     print("Hello,", name)
# greet("Diana")

# 3. Написать функцию square(n), которая возвращает квадрат числа.
# def square(n):
#     return n * n
# print(square(6))

# 4. Написать функцию is_even(num), которая возвращает True, если число чётное.
# def is_even(num):
#     return num % 2 == 0
# print(is_even(10))

# 5. Функция sum_list(nums) должна вернуть сумму чисел списка.
# def sum_list(nums):
#     return sum(nums)
# print(sum_list([1, 2, 3, 4, 5]))

# # 6. Функция first_letter(word) должна вернуть первую букву строки.
# def first_letter(word):
#     return word[0] 
# print(first_letter("Diana"))

# 7. Функция big_words(words) принимает список строк и возвращает количество строк длиной > 5.
# def big_words(words):
#     total = 0
#     for word in words:
#         if len(word) > 5:
#             total += 1
#     return total
# print(big_words(["Яблоко", "сыр", "вода", "колбаса", "телевизор"]))

# 8. Функция get_age(user) принимает словарь {"name": "...", "age": ...} и возвращает возраст.
# def get_age(user):
#     return user["age"]
# print(get_age({"name": "Alice", "age": 30}))

# 9. Функция double_list(nums) должна возвращать новый список, где каждое число умножено на 2.
# def double_list(nums):
#     num_2=[]
#     for i in nums:
#         i*2
#         num_2.append(i * 2)
#     return num_2
# print(double_list([1, 2, 3, 4, 5]))

# # 10. Функция info(name, age) должна вернуть строку:
# Имя: <name>, возраст: <age>
# def info(name, age):
#     return f"Имя: {name}, возраст: {age}"
# print(info("Di", 25))