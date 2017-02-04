
class Logger(object):

    def info(self, st):
        print(st)

    def debug(self, st):
        print(st)

    def err(self, st):
        print(st)


class Logging(object):

    def __init__(self, logger):
        self._logger = logger

    def error(self, st):
        self._logger.err(st)
