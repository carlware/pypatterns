import six
import abc


class AbsAuto(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def start(self):
        """required"""

    @abc.abstractmethod
    def stop(self):
        """required"""
