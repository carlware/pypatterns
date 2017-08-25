from .handler import AbsHandler


class Window(AbsHandler):
    _name = 'window'

    def execute(self, request):
        request.state += 1
        print("open window-{}".format(request.name))


class Dialog(AbsHandler):
    _name = 'dialog'

    def execute(self, request):
        request.state += 1
        print("open dialog-{}".format(request.name))


class Action(AbsHandler):
    _name = 'action'

    def execute(self, request):
        if request.state > 5:
            print("Action trigger for {}".format(request.name))
