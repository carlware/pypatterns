import datetime
from six import StringIO


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


class Logger(object):
    log_file = None

    def open_log(self):
        self.log_file = StringIO()

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '{}: {}'.format(now, log_record)
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close()

    def show_log(self):
        return self.log_file.getvalue()
