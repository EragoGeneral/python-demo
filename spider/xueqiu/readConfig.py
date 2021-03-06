import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")
print(configPath)

class ReadConfig:
    def __init__(self):
        fd = open(configPath, encoding="utf-8")
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def Mysql(self, name):
        value = self.cf.get("Mysql", name)
        return value

    def Database(self, name):
        value = self.cf.get("DATABASE", name)
        return value