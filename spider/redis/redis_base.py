from redis import StrictRedis, ConnectionPool

redis = StrictRedis(host='localhost', port=6379, db=0, password='123456')

redis.set('name', 'Bob')
print(redis.get('name'))

pool = ConnectionPool(host='localhost', port=6379, db=0, password='123456')
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))


url = 'redis://:123456@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
# 是否存在
print(redis.exists('name'))
print(type('name'))
# 删除 key
#print(redis.delete('name'))
print(redis.exists('name'))

print(redis.dbsize())

print(redis.randomkey())

# 重命名
#print(redis.rename('zon', 'district'))

#redis.set('district', 'PS')
# 设置超时
print(redis.expire('district', 100))
#获取剩余时间
print(redis.ttl('district'))

print(redis.move('name', 3))

print(redis.mget(['country', 'province']))



