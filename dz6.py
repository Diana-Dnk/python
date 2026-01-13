# print("------Мини касса------")
# total=0
# while True:
#     menu=print("Введите цифру:","\n1-добавить товар", "\n2-показать общую сумму", "\n3-оплатить корзину","\n0-выход")
#     data=input("Выберите пункт: ")
#     if data =="0":
#         break
#     if data =="":
#         continue
#     num=float(data)
#     if num==1:
#         product=input("Введите название товара: ")
#         price=int(input("Введите цену: "))
#         if price<0:
#             print("Цена не может быть меньше 0")
#             continue 
#         total+=price
#         print("Товар добавлен! Текущая сумма:", total)
#     if num==2:
#         print("Общая сумма корзины:", total)
#     if num==3:
#         question=input("Вы хотите оплатить товар? да/нет: ")
#         if question=="да":
#             print("Итого к оплате:",total,"\nОплачено!")
#             total=0
#         else:
#             print("Оплата отменена")
# print("Итог:",total)






