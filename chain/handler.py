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

    def run(self, request):
        self.execute(request=request)
        if self.next_handler is not None:
            self.next_handler.run(request=request)


class Window(AbsHandler):

    def execute(self, request):
        """

        :param request (Request):
        :return:
        """
        request.state += 1
        print("open window-{}".format(request.name))


class Dialog(AbsHandler):

    def execute(self, request):
        request.state += 1
        print("open dialog-{}".format(request.name))


class Action(AbsHandler):

    def execute(self, request):
        if request.state > 5:
            print("Action trigger for {}".format(request.name))
