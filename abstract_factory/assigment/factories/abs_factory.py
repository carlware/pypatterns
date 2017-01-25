import six
import abc


class AbsFactory(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def create_commercial(self):
        """required"""

    @abc.abstractmethod
    def create_retail(self):
        """required"""

    @abc.abstractmethod
    def create_government(self):
        """required"""
