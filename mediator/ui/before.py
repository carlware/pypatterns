

class TextField(object):

    def __init__(self):
        self.text = None

    def get_text(self):
        return self.text


class ListItem(object):

    def __init__(self):
        self.input_text = None
        self.items = []

    def set_input_text(self, input_text):
        self.input_text = input_text

    def select_item(self, i):
        self.input_text.text = self.items[i]
