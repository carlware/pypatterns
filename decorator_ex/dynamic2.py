import six
import abc


class GraphicalComponent(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def paint(self):
        """required"""

    @abc.abstractmethod
    def add_content(self, content):
        """required"""
        return self

    def get_component(self):
        return self


class TextField(GraphicalComponent):

    def __init__(self):
        self._lines = []

    def add_content(self, content):
        self._lines.append(content)
        if len(self._lines) == 3:
            return ScrollBarDecorator(self)
        else:
            return self

    def paint(self):
        print('start textfield \n')
        for line in self._lines:
            print(line)
        print('\nend textfield')

class Decorator(six.with_metaclass(abc.ABCMeta, GraphicalComponent)):

    def __init__(self, next_c):
        # if not (isinstance(next_c, GraphicalComponent) or isinstance(next_c, Decorator)):
        #     raise TypeError('must be instance of GraphicalComponent')
        self._next = next_c

    def paint(self):
        self._next.paint()

    def add_content(self, content):
        return self

    def get_component(self):
        return self._next


class BorderDecorator(Decorator):

    def paint(self):
        print('render before text_field')
        super(BorderDecorator, self).paint()
        print('render after text_field')


class ScrollBarDecorator(Decorator):

    def paint(self):
        print('adding scrollbar')
        super(ScrollBarDecorator, self).paint()
