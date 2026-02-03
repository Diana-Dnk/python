# Задание 1. Timer
# Создать класс Timer:
# - атрибут seconds (начально 0)
# - методы:
#   add(value) — прибавляет секунды
#   reset() — сбрасывает в 0
#   get_time() — возвращает строку mm:ss

# Пример: 65 секунд → 01:05
# class Timer:
#     def __init__(self):
#         self.seconds=0   
    
#     def add (self,value):
#         if value<0:
#             print("Нельзя добавить отрицательное время")
#             return
#         self.seconds+=value

#     def reset(self):
#         self.seconds=0

#     def get_time(self):
#         minutes = self.seconds // 60
#         seconds = self.seconds % 60
#         return f"{minutes:02}:{seconds:02}"

# timer = Timer() 
# timer.add(79)
# print(timer.get_time())  
# timer.add(30)
# print(timer.get_time())
        

# Задание 2. Playlist
# Создать класс Playlist:
# - songs (список песен)
# - методы:
#   add_song(title)
#   remove_song(title)
#   count()
#   show()

# class Playlist:
#     def __init__(self):
#         self.songs=[]

#     def add_songs(self,title):
#         if title==" ":
#             print("Введите корректное название песни")
#             return
#         self.songs.append(title)

#     def remove_song(self,title):
#         if title not in self.songs:
#             print("Введите корректное название песни")
#             return
#         self.songs.remove(title)

#     def count(self):
#         return len(self.songs)
        

#     def show(self):
#         return self.songs

# playlist=Playlist()
# playlist.add_songs("Coco")
# playlist.add_songs("Yesterday")
# playlist.add_songs("Star")
# playlist.add_songs(" ")

# print(playlist.show())
# print("Количество песен:", playlist.count())

# playlist.remove_song("Coco")
# print(playlist.show())


    
# Задание 3. ShopCart
# Создать класс ShopCart:
# - items — список объектов Product
# - методы:
#   add_product(product)
#   remove_product_by_name(name)
#   get_total()

# Использовать класс Product:
# - name, price, quantity
# - get_total_price()

# class ShopCart():
#     def __init__(self):
#         self.items=[]

#     def add_product(self,name,price,quantity):
#       self.items.append({
#         "name": name,
#         "price": price,
#         "quantity": quantity
#       })

#     def remove_product_by_name(self,name):
#         for item in self.items:
#             if item["name"]==name:
#                 self.items.remove(item)
#                 return
#         print("Товар не найден")

#     def get_total(self):
#         total = 0
#         for item in self.items:
#             total+=item["price"]*item["quantity"]
#         return total
    
# cart = ShopCart()
# cart.add_product("Apple", 100, 3)
# cart.add_product("Banana", 80, 2)

# print("Итого:", cart.get_total())  

# cart.remove_product_by_name("Apple")
# print("Итого:", cart.get_total()) 
        

# Задание 4. SafeBankAccount
# Создать класс SafeBankAccount:
# - owner, balance
# - методы:
#   deposit(amount > 0)
#   withdraw(amount > 0 и <= balance)
#   get_balance()
# Если сумма некорректна — выводить 'Ошибка'.
# Критерии оценки

# class SafeBankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
        

#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount 
#             return
#         print("Сумма:",amount,"превышает баланс","Ваша баланс:",self.balance)
           
#     def get_balance(self):
#         return self.balance
    
# kaspi= SafeBankAccount("Qwerty",1000)
# kaspi.deposit(500)
# kaspi.withdraw(200)
# kaspi.withdraw(2000)

# print(kaspi.get_balance())
        
