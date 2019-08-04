import requests
import datetime
import json

def func_process_response(response):
    if response.status_code != 200:
        return False, "Сервер БД недоступен"
    else:
        try:
            return response.json()['result'][0], False
        except KeyError:
            try:
                return False, response.json()['error']['message']
            except KeyError:
                return False, "Неверный формат ответа от БД"
        else:
            return False, "Недокументируемая ошибка, обратитесь к Администратору"

def func_get_user_by_email(var_useremail):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_get_user_by_email", "params": [var_useremail]})
    response, error = func_process_response(response)
    return response, error

def func_get_user_by_email_user_id(var_useremail, var_user_id):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_get_user_by_email_user_id", "params": [var_useremail, var_user_id]})
    response, error = func_process_response(response)
    return response, error

def func_get_friend_from_friendship(var_user):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_get_friend_from_friendship", "params": [var_user]})
    response, error = func_process_response(response)
    return response, error

def func_accept_friend_from_friendship(var_user):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_accept_friend_from_friendship", "params": [var_user]})
    response, error = func_process_response(response)
    return response, error

def func_accept_aprove_friend_from_friendship(f_user_id, var_user):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_accept_aprove_friend_from_friendship", "params": [f_user_id, var_user]})
    response, error = func_process_response(response)
    return response, error

def func_search_possible_friends_users(var_user_id, var_useremail):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_search_possible_friends_users", "params": [var_user_id, var_useremail]})
    response, error = func_process_response(response)
    return response, error

def func_add_friends_users(f_user_id, var_my_user_id):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_add_friends_users", "params": [f_user_id, var_my_user_id]})
    response, error = func_process_response(response)
    return response, error

def func_accept_friend(f_user_id, my_user_id):
    response = requests.post('http://localhost:8041/tarantool_dummies',
                             json={"method": "func_accept_friend", "params": [f_user_id, my_user_id]})
    response, error = func_process_response(response)
    return response, error
