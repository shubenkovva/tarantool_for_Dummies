local shard = require('shard')
local json = require('json')

-- tarantool configuration
box.cfg {
    listen = 33021
}

box.schema.create_space('demo', {if_not_exists = true})
box.space.demo:create_index('primary',
        {parts={1, 'unsigned'}, if_not_exists=true})

box.schema.user.grant('guest', 'read,write,execute',
        'universe', nil, {if_not_exists = true})

box.schema.user.grant('guest', 'replication',
        nil, nil, {if_not_exists = true})

-- sharding configuration
shard.init {
    servers = {
        { uri = 'localhost:33021', zone = '0' },
        { uri = 'localhost:33022', zone = '1' }
    },
    login = 'guest',
    password = '',
    redundancy = 2
}

