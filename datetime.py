import datetime

def get_user_birthday():
    day = int(input("Введите день рождения (от 1 до 31): "))
    month = int(input("Введите месяц рождения (от 1 до 12): "))
    year = int(input("Введите год рождения (например, 2002): "))
    return datetime.date(year, month, day)

    # День недели выводится из словаря, т.к. встроенная функция выводит день только на английском языке
def get_weekday(date):
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return weekdays[date.weekday()]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def format_birthday(birth_date):
    return f"{birth_date.day:02} {birth_date.month:02} {birth_date.year}"

def draw_date(date):
    date_str = format_birthday(date)
    for char in date_str:
        if char == " ":
            print("  ", end="")
        else:
            print('*' * int(char), end=" ")
    print()

def main():
    birthday = get_user_birthday()
    
    # День недели
    weekday = get_weekday(birthday)
    print(f"День недели: {weekday}")
    
    # Високосный год
    leap_year = is_leap_year(birthday.year)
    if leap_year:
        print(f"{birthday.year} - високосный год.")
    else:
        print(f"{birthday.year} - не високосный год.")
    
    # Возраст
    age = calculate_age(birthday)
    print(f"Вам сейчас {age} лет.")
    
    # Вывод даты в формате звёздочек
    print("Ваша дата рождения в формате звёздочек:")
    draw_date(birthday)

if __name__ == "__main__":
    main()
