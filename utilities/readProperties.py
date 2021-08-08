import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicaionURL():
        url=config.get('common info','baseURL')
        return url
    def getUseremail():
        username=config.get('common info','useremail')
        return username
    def getPassword():
        password=config.get('common info','password')
        return password
