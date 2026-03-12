import configparser
import os


config = configparser.RawConfigParser()
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
config_path = os.path.join(project_root,"configration","config.ini")
config.read(config_path)

class read_config():
    
    @staticmethod
    def get_url():
        url = config.get("login information","url")
        return url


    @staticmethod
    def get_username():
        username = config.get("login information","username")
        return username
    
    @staticmethod
    def get_password():
        password = config.get("login information","password")
        return password
    

