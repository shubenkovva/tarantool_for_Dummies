def application(environ, start_response):
    import requests
    import os
    from subprocess import PIPE, run
    import urllib.parse
    import json

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    data = json.loads(request_body)

    start_response('200 OK', [('Content-Type', 'text/html')])
    return str(data).encode("utf-8")

'''    response = requests.post('http://localhost:8041/tarantool_dummies',
                         json={"method": "insert_obj", "params": ['file_path', '/Users/user/Geekbrains/DataBase/tarantool_for_Dummies/' + filename]})
    if response.status_code != 200:
        s = {'status from DB': "Сервер БД недоступен"}
    else:
        s = {'status from DB': response.json()}

    def out(command):
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        return result.stdout

    my_output = out("ls -ltr")'''
