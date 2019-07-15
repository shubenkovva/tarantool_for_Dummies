'''
2)Спроектируйте базу данных, которая позволяла бы организовать хранение медиа-файлов,
загружаемых пользователем (фото, аудио, видео).
Сами файлы будут храниться в файловой системе,
а база данных будет хранить только пути к файлам, названия, описания,
ключевых слов и принадлежности пользователю.
'''
def application(environ, start_response):
    import requests
    import os
    from subprocess import PIPE, run
    #   start_response('200 OK', [('Content-Type', 'text/html')])
    #   import urllib.parse
    #   from cgi import parse_qs, escape
    #   post_input = urllib.parse.parse_qs(environ['wsgi.input'].readline().decode(),True)

    u = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
    filename = environ['HTTP_ZFILENAME']
    f = open(filename, 'wb')
    f.write(u)
    f.close()

    response = requests.post('http://localhost:8040/tarantool_dummies',
                         json={"method": "insert_obj", "params": ['file_path', '/Users/user/Geekbrains/DataBase/tarantool_for_Dummies/' + filename]})
    if response.status_code != 200:
        s = {'status from DB': "Сервер БД недоступен"}
    else:
        s = {'status from DB': response.json()}

    def out(command):
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        return result.stdout

    my_output = out("ls -ltr")
    start_response('200 OK', [('Content-Type', 'text/html')])

    return str(s['status from DB']).encode("utf-8")