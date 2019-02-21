from logger_file import Logger

class Log(Logger):
    '''
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dir = "logs/"
        self.file = self.dir + self.file
        if self.debug_file:
            self.debug_file = self.dir + self.debug_file

Logger = Log(debug_file='debug/raju.log')
logger = Logger.get_logger()
logger.debug("hello")
