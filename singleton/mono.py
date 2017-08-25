import datetime
from six import StringIO


class MonoState(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls).__new__(*args, **kwargs)
        obj.__dict__ = cls._state
        return obj


class Logger(MonoState):
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
