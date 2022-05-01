"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

user_list = []

def user_info (user_list):
    name = input(f"Hi, what is your name?")
    last_name = input(f" and last name")
    b_day = input(f"What is the date of your birthday?")
    city = input(f"where are you from ?")
    e_mail = input(f"Insert your e-mail")
    phone = input(f"Insert your phone")
    user_list = [name, last_name, b_day, city, e_mail, phone]
    return user_list
    user_list.append(name)
    user_list.append(last_name)
    user_list.append(b_day)
    user_list.append(city)
    user_list.append(e_mail)
    user_list.append(phone)


print(user_info(user_list))

