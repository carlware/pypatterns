import six
import abc

class AbsFactory(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def create_auto(self):
        """required"""