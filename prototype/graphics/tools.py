import copy
from abs_graphic import Graphic


class Video(Graphic):

    def __init__(self, url):
        self.url = url

    def clone(self):
        return Video(self.url)

    def get_state(self):
        return self.url


class Image(Graphic):

    def __init__(self, url):
        self.url = url

    def clone(self):
        # more pythonic way
        return copy.deepcopy(self)

    def get_state(self):
        return self.url


class GraphicTool(object):

    def __init__(self, proto):
        self.graphic = proto

    def create_tool(self):
        return self.graphic.clone()
