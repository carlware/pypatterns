import abc
import six


class AbsFactory(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def create_sport(self):
        """required"""

    @abc.abstractmethod
    def create_luxury(self):
        """required"""

    @abc.abstractmethod
    def create_economy(self):
        """required"""
