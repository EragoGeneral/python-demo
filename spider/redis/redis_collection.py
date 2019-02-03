from redis import  StrictRedis, ConnectionPool

url = 'redis://:123456@localhost:6379/1'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

# 集合操作
result = redis.srem('tag', 'Coffee')
print(result)

result = redis.sadd('tags', 'Book', 'Tea', 'Coffee')
print(result)

redis.set('name', '123')
print(redis.get('name'))