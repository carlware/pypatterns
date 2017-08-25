

class MyClass(object):

    def do_something(self):
        print("my class")


class MyObjectFactory(object):

    @staticmethod
    def create_object(value):
        if value == 'myclass':
            return MyClass()
        else:
            return None
