tarantoolctl stop mysql_db
nginx -s stop
cp db_config/mysql_db.lua /usr/local/Cellar/tarantool/1.10.2.1_2/share/tarantool
cp db_config/mysql_app_db.lua /usr/local/etc/tarantool/instances.available/
cp nginx_wsgi.conf nginx_tarantool_for_Dummies.conf /usr/local/openresty/nginx/conf/
rm -rf /usr/local/var/lib/tarantool/mysql_db/*
tarantoolctl start mysql_db
nginx