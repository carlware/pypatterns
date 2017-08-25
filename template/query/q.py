import abc
import six
from .conn import Connection


class TemplateQuery(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def get_query_string(self):
        return ''

    def execute(self):
        conn = Connection()
        conn.open()
        result = conn.execute(self.get_query_string())
        conn.close()
        return result
