---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by user.
--- DateTime: 2019-04-29 19:14
---
db = require('mysql_app_db_lab2')
log = require('log')

box.cfg
    {   listen=33005,
        background=true,
        log_level=5
    }

db:start()
