import abc
import six


class AbsCust(six.with_metaclass(abc.ABCMeta)):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @name.setter
    @abc.abstractmethod
    def name(self, name):
        pass

    @abc.abstractmethod
    def send_invoice(self):
        pass
