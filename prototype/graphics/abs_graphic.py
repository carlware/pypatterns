import abc
import six


class Graphic(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def clone(self):
        """required"""
        
    @abc.abstractmethod
    def get_state(self):
        """required"""
