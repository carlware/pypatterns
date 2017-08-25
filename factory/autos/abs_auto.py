import abc
import six


class AutoAbs(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def start(self):
        """required"""

    @abc.abstractmethod
    def stop(self):
        """required"""