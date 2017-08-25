import abc
import six


class TextField(object):

    def __init__(self):
        self.text = None

    def get_text(self):
        return self.text


class MediatorList(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def item_selected(self, item):
        """"""


class MediatorListTextInput(MediatorList):

    def __init__(self):
        self.text = None

    def item_selected(self, item):
        self.text.text = item

    def set_text_input(self, text_input):
        self.text = text_input


class ListItem(object):

    def __init__(self):
        self.mediator = None
        self.items = []
        self.selected_item = None

    def set_mediator(self, input_text):
        self.mediator = input_text

    def select_item(self, i):
        self.selected_item = self.items[i]
        if self.mediator is not None:
            self.mediator.item_selected(self.selected_item)
