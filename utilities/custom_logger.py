import logging
import datetime



class log_maker():
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".//logs//valid_login.log",level= logging.INFO,format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',datefmt='%Y-%m-%d %H:%M:%S',force=True)
        logger = logging.getLogger("Swag Labs test logs")
        logger.setLevel(logging.INFO)
        return logger