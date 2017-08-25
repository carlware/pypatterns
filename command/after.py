import six
import abc


class Command(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def execute(self):
        pass

    def undo(self):
        pass


class CommandMeta(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def description(self):
        pass


class UpdateOrder(Command, CommandMeta):
    name = 'UpdateOrder'
    description = 'Update Quantity Number'

    def __init__(self, args):
        self.quantity = args[1]

    def execute(self):
        old_val = 5
        val = self.quantity
        print("Database Updated")
        print("Logging updated quantity from %s to %s" % (old_val, val))


class NoCommand(Command):

    def __init__(self, args):
        self.name = args[0]

    def execute(self):
        print("No command named: {}".format(self.name))


def get_commands():
    commands = [UpdateOrder]
    return dict([c.name, c] for c in commands)


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)
