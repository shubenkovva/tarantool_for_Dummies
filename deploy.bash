tarantoolctl stop mysql_db
tarantoolctl stop mysql_db_lab2
tarantoolctl stop shard_db_lab3
nginx -s stop
cp lab1/db_config/mysql_app_db.lua /usr/local/Cellar/tarantool/1.10.2.1_2/share/tarantool
cp lab1/db_config/mysql_db.lua /usr/local/etc/tarantool/instances.available/
#
cp lab2/db_config/mysql_app_db_lab2.lua /usr/local/Cellar/tarantool/1.10.2.1_2/share/tarantool
cp lab2/db_config/mysql_db_lab2.lua /usr/local/etc/tarantool/instances.available/
#
cp lab3/db_config/shard_app_db_lab3.lua /usr/local/Cellar/tarantool/1.10.2.1_2/share/tarantool
cp lab3/db_config/shard_db_lab3.lua /usr/local/etc/tarantool/instances.available/
#
cp nginx_wsgi.conf nginx_tarantool_for_Dummies.conf /usr/local/openresty/nginx/conf/
#rm -rf /usr/local/var/lib/tarantool/mysql_db/*
#rm -rf /usr/local/var/lib/tarantool/mysql_db_lab2/*
rm -rf /usr/local/var/lib/tarantool/shard_db_lab3/*
tarantoolctl start mysql_db
tarantoolctl start mysql_db_lab2
tarantoolctl start shard_db_lab3
nginx