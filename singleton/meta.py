import datetime
from six import StringIO
import six
import abc


class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args)
        return cls.__instance


class Logger(six.with_metaclass(Singleton)):
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
