import datetime
from six import StringIO


class Logger(object):
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

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
