import configparser

config = configparser.RawConfigParser()
config.read("C://Users//DELL//PycharmProjects//Test FrameworkDemo//configurations//Config.ini")


class ReadConfig:

    @staticmethod
    def getUrl():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
