import abc
import six


class Request(object):

    def __init__(self, state, name=''):
        self.state = state
        self.name = name


class AbsHandler(six.with_metaclass(abc.ABCMeta)):

    def __init__(self, handler=None):
        self.next_handler = handler  # type: AbsHandler

    @abc.abstractmethod
    def execute(self, request):
        """required"""
        # type: Request

    def run(self, request):
        self.execute(request=request)
        if self.next_handler is not None:
            self.next_handler.run(request=request)


class DefaultHandler(AbsHandler):
    def execute(self, request):
        print("unimplemented handler {}".format(request.name))
