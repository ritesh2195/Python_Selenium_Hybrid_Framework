import configparser

config = configparser.RawConfigParser()
config.read(".\\Confugrations\\config.ini")


class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common info', 'Email')
        return email

    @staticmethod
    def getPassword():
        password=config.get('common info','Password')

        return password

