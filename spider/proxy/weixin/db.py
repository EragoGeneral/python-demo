from pickle import dumps, loads
from request import WeixinRequest
from redis import StrictRedis
from config import *

class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request):
        """
        向队列添加序列化后的 request
        :param request: 请求对象
        :return:
        """
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))

        return False

    def pop(self):
        """
        取出下一个 Request 并反序列化
        :return:    Request or None
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0