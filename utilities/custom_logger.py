import logging

class LogMaker:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename= "./logs/swaglabs.log", format= '%(asctime)s:%(levelname)s:%(message)s',datefmt= "%Y-%m-%d %H:%M:%S",force= True)

        logger = logging.getLogger()
## If anything is critical then we can use 'warning' before 'info' for taking the log
        logger.setLevel(logging.WARNING)
        return logger

    @staticmethod
    def log_gen1():
        logging.basicConfig(filename= "./logs/swaglabs.log", format= '%(asctime)s:%(levelname)s:%(message)s',datefmt= "%Y-%m-%d %H:%M:%S",force= True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger