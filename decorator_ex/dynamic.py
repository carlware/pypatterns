import six
import abc
from inspect import isabstract


class GraphicalComponent(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def paint(self):
        """required"""

    @abc.abstractmethod
    def add_content(self, content):
        """required"""

    def get_component(self):
        return self


class TextField(GraphicalComponent):

    def __init__(self):
        self._lines = []

    def add_content(self, content):
        self._lines.append(content)

    def paint(self):
        print('start textfield \n')
        for line in self._lines:
            print(line)
        print('\nend textfield')

    def get_lines(self):
        return self._lines


class Decorator(six.with_metaclass(abc.ABCMeta, GraphicalComponent)):

    def __init__(self, next_c):
        if not isinstance(next_c, GraphicalComponent):
            raise TypeError('must be instance of GraphicalComponent')
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
        print('scrollbar decorator init')
        component = super(ScrollBarDecorator, self).get_component()
        components = []

        while isinstance(component, GraphicalComponent):
            components.append(component)
            component = component.get_component()

            if isinstance(component, TextField) and len(component.get_lines()) >= 3:
                print('adding scrollbar')
                break
            # root graphical component does not have next so break chain decorator
            if isinstance(component, GraphicalComponent):
                break

        for comp in reversed(components):
            comp.paint()
