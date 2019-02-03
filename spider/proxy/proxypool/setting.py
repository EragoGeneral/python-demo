# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 123456

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

VALID_STATUS_CODES = [200, 302]

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://weixin.sogou.com/weixin?type=2&query=NBA'

# 最大批测试量
BATCH_TEST_SIZE = 10

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# API配置
API_HOST = '127.0.0.1'
API_PORT = 5555