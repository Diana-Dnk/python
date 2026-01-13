# Задание 1. Регистрация пользователя
# # Функция register_user(username, password).
# # check_username() — имя не пустое 
# # check_password() — длина ≥ 8
# # Результат: «Регистрация успешна» / «Ошибка регистрации»
# def register_user(username, password):
#     def check_username():
#         return username!=" "
#     def check_password():
#         return len(password)>=8
#     if check_username() and check_password():
#         return "Регистрация успешна"
#     else:
#         return "Ошибка регистрации"
# print(register_user("Di","123456789"))
# print(register_user(" ","123456789"))
# print(register_user(" ","1234567"))
      

# Задание 2. Проверка заказа
# Функция check_order(quantity, in_stock).
# check_quantity() — количество > 0
# check_stock() — товар в наличии
# Результат: «Заказ принят» / «Заказ отклонён»
# def check_order(quantity, in_stock):
#     def check_quantity():
#         return quantity>0
#     def check_stock():
#         return in_stock=="Товар в наличии"
#     if check_quantity() and check_stock():
#         return "Заказ принят"
#     else:
#         return "Заказ отклонен"
# print(check_order(2,"Товар в наличии"))
# print(check_order(0,"Товар в наличии"))
# print(check_order(5,"Товара нет в наличии"))

# Задание 3. Проверка оценки
# Функция check_grade(score).
# is_number() — значение число
# is_valid_range() — от 0 до 100
# Результат: «Оценка принята» / «Некорректная оценка»
# def check_grade(score):
#     def is_number():
#         return type(score)==int
#     def is_valid_range():
#         return score>=0 and score<=100
#     if is_number() and is_valid_range():
#         return "Оценка принята"
#     else: 
#         return "Некорректная оценка"
# print(check_grade(50))
# print(check_grade("50"))
# print(check_grade(299))

# Задание 4. Доступ к системе
# Функция system_access(role, is_active).
# check_role() — admin или manager
# check_status() — активен
# Результат: «Доступ открыт» / «Доступ запрещён»
# def system_access(role, is_active):
#     def check_role():
#         return role=="admin" or role=="manager"
#     def check_status():
#         return is_active=="active"
#     if check_role() and check_status():
#         return "Доступ открыт"
#     else: 
#         return "Доступ запрещен"
# print(system_access("admin","active"))
# print(system_access("user","active"))
# print(system_access("manager","active"))
# print(system_access("admin","inactive"))

# Задание 5. Проверка оплаты
# Функция check_payment(amount, balance).
# check_amount() — сумма > 0
# check_balance() — баланс ≥ суммы
# Результат: «Оплата прошла» / «Недостаточно средств»
def check_payment(amount, balance):
    def check_amount():
        return amount>0
    def check_balance():
        return balance>=amount
    if check_amount() and check_balance():
        return "Оплата прошла"
    else:
        return "Недостаточно средств"
print(check_payment(1000,3000))
print(check_payment(0,3000))
print(check_payment(5000,3000))