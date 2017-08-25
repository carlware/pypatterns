from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .handler import AbsHandler, DefaultHandler


class Loader(object):
    _handlers = None

    @classmethod
    def load_handler(cls, name):
        if cls._handlers is not None:
            if name not in cls._handlers:
                return DefaultHandler
            return cls._handlers[name]
        else:
            factory_module = import_module('.handlers', 'chain.client')
            classes = getmembers(factory_module,
                                 lambda m: isclass(m) and not isabstract(m))

            cls._handlers = dict()
            for c_name, _class in classes:
                if issubclass(_class, AbsHandler):
                    cls._handlers[_class._name] = _class

            return cls.load_handler(name)


class Client(object):

    def __init__(self, request, names=None, loader=Loader):
        self.request = request
        self.names = names or []
        self.c_Loader = loader  # type: Loader

    def run(self):
        for name in self.names:
            handler = Loader.load_handler(name)()
            handler.execute(self.request)

