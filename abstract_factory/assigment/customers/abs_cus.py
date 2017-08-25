import abc
import six


class AbsCust(six.with_metaclass(abc.ABCMeta)):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def report_type(self):
        """required"""
