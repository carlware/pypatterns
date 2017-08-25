import six
import abc


class AbsClass(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def do_something(self):
        """required"""


class NullClass(AbsClass):

    def do_something(self):
        print("null object")


class MyObject(AbsClass):

    def do_something(self):
        print("my object ...")


class SimpleFactory(object):

    def create_obj(self, name):
        if name == 'class':
            return MyObject()
        else:
            return NullClass()
