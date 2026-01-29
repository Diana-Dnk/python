# Задание 1 — Калькулятор деления (исключения)
# Сделать программу, которая:
# 1) Просит у пользователя два числа a и b.
# 2) Печатает результат a / b.
# 3) Обрабатывает ошибки: ValueError (ввод не число), ZeroDivisionError (b=0).
# 4) В finally печатает: 'Завершено'.
# Требование: отдельные except для ValueError и ZeroDivisionError.

# print("Калькулятор деления")
# try:
#     a = int(input("Введите число a: "))
#     b = int(input("Введите число b: "))
#     result = a / b
#     print("Результат:", result)
# except ValueError:
#     print("Ошибка: введено не число")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль невозможно")
# finally:
#     print("Завершено")

# Задание 2 — Excel: товары и отчёт
# Создай файл products.xlsx со столбцами: ID, Title, Price, Quantity.
# Напиши скрипт, который:
# 1) Читает products.xlsx.
# 2) Для каждой строки делает объект Product.
# 3) Если Price/Quantity пустые или кривые — строку пропускает (через except (ValueError, TypeError)).
# 4) Сохраняет products_report.xlsx с колонками: Title, LineTotal.
# 5) Внизу отчёта добавляет строку 'TOTAL' и общую сумму.
# from openpyxl import Workbook, load_workbook
# class Product:
#     def __init__(self, title, price, quantity):
#         self.title = title
#         self.price = price
#         self.quantity = quantity
#     def line_total(self):
#         return self.price * self.quantity


# wb = Workbook()
# sheet = wb.active
# sheet.title = "Products"

# sheet.append(["ID", "Title", "Price", "Quantity"])
# sheet.append([1, "клавиатура", 12000, 2])
# sheet.append([2, "мыщка", 5000, 3])
# sheet.append([3, "монитор", "abc", 1])   
# sheet.append([4, "наушники", 8000, None])  

# wb.save("products.xlsx")

# wb = load_workbook("products.xlsx")
# sheet = wb.active

# products = []

# for row in sheet.iter_rows(min_row=2, values_only=True):
#     _, title, price, quantity = row
#     try:
#         price = float(price)
#         quantity = int(quantity)
#         product = Product(title, price, quantity)
#         products.append(product)
#     except (ValueError, TypeError):
#         continue

# report_wb = Workbook()
# report_sheet = report_wb.active
# report_sheet.title = "Report"

# report_sheet.append(["Title", "LineTotal"])

# total_sum = 0

# for product in products:
#     line_total = product.line_total()
#     total_sum += line_total
#     report_sheet.append([product.title, line_total])

# report_sheet.append(["TOTAL", total_sum])
# report_wb.save("products_report.xlsx")


# Задание 3 — Excel: студенты и средний балл
# Создай students2.xlsx со столбцами: ID, Name, Score1, Score2, Score3.
# Скрипт должен:
# 1) Для каждой строки создать объект Student.
# 2) Добавить оценки через add_score.
# 3) Посчитать avg() и сохранить report_students.xlsx: Name, Avg.
# 4) Обработать кривые значения (None, '—', 'abc') через (ValueError, TypeError).

# from openpyxl import load_workbook, Workbook

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.scores = []

#     def add_score(self, score):
#         try:
#             score = float(score)
#             self.scores.append(score)
#         except (ValueError, TypeError):
#             pass  

#     def avg(self):
#         if not self.scores:
#             return 0
#         return round(sum(self.scores) / len(self.scores), 2)

# wb = Workbook()
# ws = wb.active
# ws.title = "Students"
# ws.append(["ID", "Name", "Score1", "Score2", "Score3"])
# ws.append([1, "Anna", 90, 85, 88])
# ws.append([2, "Max", 100, "—", "abc"])
# ws.append([3, "Kate", 70, None, 80])
# ws.append([4, "John", "abc", "—", None])

# wb.save("students2.xlsx")

# wb = load_workbook("students2.xlsx")
# ws = wb.active
# students = []
# for row in ws.iter_rows(min_row=2, values_only=True):
#     _, name, s1, s2, s3 = row

#     student = Student(name)
#     student.add_score(s1)
#     student.add_score(s2)
#     student.add_score(s3)

#     students.append(student)

# report_wb = Workbook()
# report_ws = report_wb.active
# report_ws.title = "Report"

# report_ws.append(["Name", "Avg"])

# for student in students:
#     report_ws.append([student.name, student.avg()])

# report_wb.save("report_students.xlsx")
# print("Файл students2.xlsx и report_students.xlsx созданы")
