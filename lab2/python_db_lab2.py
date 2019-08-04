import requests
import datetime
import json
import python_db_lab2_func as fl

class User:
    def __init__(self, var_user_gl, var_profile_gl):
        self.var_user_gl = var_user_gl
        self.var_profile_gl = var_profile_gl
    def refresh_my_data(self):
        result, error = fl.func_get_user_by_email(self.var_user_gl[3])
        if result is None and not error:
            print("Введенное имя пользователя не существует = " + self.var_user_gl[3])
        elif error:
            print("Произошла ошибка " + error)
i = 0
while i == 0:
    usermail = str(input("Введите email пользовтеля для авторизации:"))
    result, error = fl.func_get_user_by_email(usermail)
    if result is None and not error:
        print("Введенное имя пользователя не существует = " + usermail)
    elif error:
        print("Произошла ошибка " + error)
    else:
        print("Вы успешно авторизованы " + str(result['Users']))
        cl_my_user = User(result['Users'], result['Profiles'])
        print('User email=' + cl_my_user.var_user_gl[3] + ' User_ID=' + str(cl_my_user.var_user_gl[0]))
        i = 1
answer = ''
while answer != 'q':
    print("[1] -  Напечатать информацию о себе")
    print("[2] -  Вывести список друзей")
    print("[3] -  Добавить друга")
    print("[4] -  Принять друга")
    try:
        do = int(input("Укажите номер действия: "))
    except ValueError:
        do = 0
    if do == 1:
        cl_my_user.refresh_my_data()
        print(cl_my_user.var_user_gl)
        print(cl_my_user.var_profile_gl)

    elif do == 2:
        result, error = fl.func_get_friend_from_friendship(cl_my_user.var_user_gl[0])
        if result is None and not error:
            print("У вас нет друзей")
        elif error:
            print("Произошла ошибка " + error)
        else:
            for i in result:
                print(i)
    elif do == 3:
        var_useremail = str(input("Введите email или его часть:"))
        while not var_useremail:
            print('Введенное имя пользователя не существует, введите корректное имя пользователя')
            var_useremail = str(input("Введите email или его часть:"))
        result, error = fl.func_search_possible_friends_users(cl_my_user.var_user_gl[0], var_useremail)
        if result is None and not error:
            print('Для указаннго "' + var_useremail + '" не существует контакта')
        elif error:
            print("Произошла ошибка " + error)
        else:
            for i in result:
                print(i)
            i = 0
            while i == 0:
                try:
                    f_user_id = int(input("Введите id пользователя для запроса в друзья: "))
                    i = 1
                except ValueError:
                    print('Введите корректное id пользователя')
            result, error = fl.func_add_friends_users(f_user_id, cl_my_user.var_user_gl[0])
            if result is None and not error:
                print('Для указаннго "' + f_user_id + '" не существует контакта')
            elif error:
                print("Произошла ошибка " + error)
            else:
                print("Статус запроса в друзья: ")
                print(result)
    elif do == 4:
        result, error = fl.func_accept_friend_from_friendship(cl_my_user.var_user_gl[0])
        if result is None and not error:
            print("У вас запросов в друзья")
        elif error:
            print("Произошла ошибка " + error)
        else:
            for i in result:
                print(i)
        i = 0
        while i == 0:
            try:
                f_user_id = int(input("Введите id пользователя для запроса в друзья: "))
                i = 1
            except ValueError:
                print('Введите корректное id пользователя')
            result, error = fl.func_accept_aprove_friend_from_friendship(f_user_id, cl_my_user.var_user_gl[0])
            if result is None and not error:
                print("Id не существует")
            elif error:
                print("Произошла ошибка " + error)
            else:
                print(result)
    else:
        print("Вы ввели некоректную команду")
    answer = input("Введите q чтобы выйти или нажмите Enter, чтобы продолжить: ")



