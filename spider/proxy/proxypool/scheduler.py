from multiprocessing import Process
from api import app
from getter import Getter
from tester import Tester
from setting import *
import time
from db import RedisClient

class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        :return:
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')

        print('判断检测模块标识')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        print('判断抓取模块标识')
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        print('判断接口模块标识')
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()


if __name__ == '__main__':
    s = Scheduler()
    s.run()





