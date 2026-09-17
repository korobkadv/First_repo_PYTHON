from datetime import datetime
import random
import re

'''
goit-algo-hw-03
    Перше завдання
    Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
'''
def get_days_from_today(date):
    # перетворює рядок в дату, віднімає поточний час і повертає результат в днях
    return (datetime.strptime(date, "%Y-%m-%d") - datetime.now()).days

print("Кількість днів між заданою датою і поточною датою:", get_days_from_today("2021-10-09"))



'''
goit-algo-hw-03
    Друге завдання
    Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних 
    випадкових чисел.
    Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні
     бути унікальні.
'''
def get_numbers_ticket(min, max, quantity):
    # Переконуємось, що вхідні параметри відповідають заданим обмеженням
    if min < 1:
        return "Помилка: min не менше 1"
    elif max > 1000:
        return "Помилка: max не більше 1000"
    else:
        numbers = []

        # Заповнюємо неповторювані числа в межах обмежень
        while min <= max:
            numbers.append(min)
            min += 1

        # random.sample обираємо випадкові неповторювані числа.
        return random.sample(numbers, quantity)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)




'''
goit-algo-hw-03
    Третє завдання (не обов'язкове)
     Необхідна функція, яка автоматично нормалізує номери телефонів до потрібного формату, видаляючи всі зайві символи 
     та додаючи міжнародний код країни, якщо потрібно.
'''

def normalize_phone(number):
    normalized_number = re.sub(r"[^\d+]", "", str(number))
    normalized_number = re.sub(r"^38", "+38", normalized_number)
    normalized_number = re.sub(r"^0", "+380", normalized_number)
    return normalized_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
