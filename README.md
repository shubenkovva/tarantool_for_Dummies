# tarantool_for_Dummies

Инсталляция tarantool на MAC:

  brew install tarantool (https://www.tarantool.io/ru/download/os-installation/1.10/os-x/)
  
Инсталляция модуля upstream для nginx:

  https://github.com/tarantool/nginx_upstream_module
  В моем случае я использувал сборку nginx openresty (https://github.com/openresty/lua-nginx-module). После того как скачали и распаковали проект openresty в него нужно поместить nginx_upstream_module и при сборке указать его:
  
   ./configure --prefix=/opt/nginx \
         --with-ld-opt="-Wl,-rpath,/path/to/luajit-or-lua/lib" \
         --add-module=/path/to/ngx_devel_kit \
         --add-module=/path/to/lua-nginx-module
         --with-tarantool-module
  
Конфигруционные файлы tarantool:

  /usr/local/Cellar/tarantool/1.10.2.1_2/share/tarantool - конфиг БД
  /usr/local/etc/tarantool/instances.available/ - конфиг прилодения БД
