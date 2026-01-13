# 1. Добавьте число 999 в конец списка с помощью метода append().
# nums=[1,2,3,56,524,6,34]
# nums.append(999)
# print("новый список:",nums)

# 2. Удалите из списка все элементы, равные 0, используя remove() и цикл while.
# nums=[1,4,0,7,6,9,0,54,0,675,0,8,9,0]
# zero=0
# while zero in nums:
#     nums.remove(zero)
# print("без 0:", nums)

# 3. Посчитайте количество элементов со значением 5, используя count().
# nums=[1,2,45,65,4,5,4,5,32,5,5,5,7,5]
# count=nums.count(5)
# print(count)

# 4. Создайте новый список — перевёрнутую копию исходного.
# nums=[1,2,3,4,5,6,7,8,9,10]
# nums_copy=nums.copy()
# nums_copy.reverse()
# print("Исходный:",nums)
# print("Новый:",nums_copy)

# 5. Разделите список на два: evens (чётные) и odds (нечётные).
# nums=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for i in nums:
#     if i%2==0:
#         even.append(i)
#     if i%2==1:
#         odd.append(i)
# print(even)
# print(odd)

# 6. Удалите все числа меньше 10, используя pop() в цикле.
# nums=[1,10,24,5,245,3,4,21,10,23,3,6]
# i = 0
# while i < len(nums):
#     if nums[i] < 10:
#         nums.pop(i)   
#     else:
#         i += 1        
# print(nums)

# 7.	7. Найдите три минимальных числа без изменения исходного списка.
# nums = [1,2,7,34,6,7,4,67,8,0]
# min_nums = sorted(nums)[:3]
# print(min_nums)

# 8.	8. Объедините два списка методом extend().
# a=[1,2,3,56,36,24,52,1,0]
# b=[True,False,"qwerty",34]
# a.extend(b)
# print(a)

# 9.	9. Найдите среднее значение списка и создайте список элементов, которые больше среднего.
# nums=[1,2,3,4,5,6,7,8,9,10]
# a=sum(nums)/len(nums)
# print("Седнее число:",a)
# i=0
# while i<len(nums):
#     if nums[i]<a:
#         nums.pop(i)   
#     else:
#         i += 1        
# print("Числа больше среднего:",nums)

# 10. Удалите все максимальные значения из списка.
# nums=[1,2,445,645,3,36,67,7]
# num_max=max(nums)
# while num_max in nums:
#     nums.remove(num_max)
# print(nums)

# 11.	11. Создайте новый список: сначала отрицательные числа, затем остальные.
# nums=[1,23,-3,5,-35,-5,235,-57,3,46,4]
# a=[]
# b=[]
# for i in nums:
#     if i>0:
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)

# 12.	12. Для списка заказов [id, цена]: найдите сумму, минимальную цену и её id.
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