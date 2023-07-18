import logging

class Loggen:


    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename="C:/Users/DELL/PycharmProjects/Test FrameworkDemo/logs/automation.log", mode="a")
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s", datefmt="%m/%d/%Y %I:%M:%S")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        return logger