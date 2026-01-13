# # mini-project
# # это база
# products=[]
# # функция добавления товара
# def add_product(name,price,quantity):
#     product={
#         "name": name,
#         "price": price,
#         "quantity":quantity
#     }
#     products.append(product)

# # фунция поиска товара
# def find_product(name):
#     for product in products:
#         if product["name"].lower()==name.lower():
#             return product
#     return None

# # функция вывода товара 
# def show_products():
#     if len(products)==0:
#         print("Товаров нет")
#         return
#     index=1
#     for product in products:
#         print(index,".",product["name"],"-",product["price"],"X",product["quantity"],"T")
#         index+=1
# # Функция подсчета общей суммы 
# def get_total_price():
#     total=0
#     for product in products:
#         total+=product["price"]*product["quantity"]
#     return total

# # функция меню
# def show_menu():
#     print("1. Добавить товар")
#     print("2. Показать товары")
#     print("3. Добавить общую сумму")
#     print("4. Поиск товара")
#     print("0. Выход")

# while(True):
#     show_menu()
#     choice=input("Выберите действие: ")
#     if choice=="1":
#         name=input("Название товара: ")
#         price=int(input("Цена товара: "))
#         quantity=int(input("Введите количество: "))
#         add_product(name,price,quantity)
#     elif choice=="2":
#         show_products()
#     elif choice=="3":
#         total=get_total_price()
#         print("Общая сумма:",total,"Тенге")
#     elif choice=="4":
#         name=input("Введите название товара для поиска: ")
#         product=find_product(name)
#         if product:
#             print("Товар найден:", product)
#         else:
#             print("Товар не найден")
#     elif choice=="0":
#         print("Выход из системы")
#         break
#     else:
#         print("Неверный выбор")