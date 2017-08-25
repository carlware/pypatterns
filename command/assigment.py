import six
import abc
from Queue import LifoQueue
from collections import defaultdict

# Appliances
class Appliance(object):
    def __init__(self, name):
        self._name = name

    def on(self):
        print('{} has been turned on.'.format(self._name))

    def off(self):
        print('{} has been turned off.'.format(self._name))


class Door(object):
    def __init__(self, name):
        self.name = name

    def lock(self):
        print('{} is locked.'.format(self.name))

    def unlock(self):
        print('{} is unlocked.'.format(self.name))


class Security(object):
    def arm(self):
        print('Security system armed')

    def disarm(self):
        print('Security disarmed')


class AbsCommand(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class ApplianceOnCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError()
        self.appliance = appliance

    def execute(self):
        self.appliance.on()

    def undo(self):
        self.appliance.off()


class ApplianceOffCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError()
        self.appliance = appliance

    def execute(self):
        self.appliance.off()

    def undo(self):
        self.appliance.on()


class DoorLockCommand(AbsCommand):
    def __init__(self, door):
        if not isinstance(door, Door):
            raise TypeError()
        self.door = door

    def execute(self):
        self.door.lock()

    def undo(self):
        self.door.unlock()


class DoorUnlockCommand(AbsCommand):
    def __init__(self, door):
        if not isinstance(door, Door):
            raise TypeError()
        self.door = door

    def execute(self):
        self.door.unlock()

    def undo(self):
        self.door.lock()


class SecurityArmCommand(AbsCommand):
    def __init__(self, security):
        if not isinstance(security, Security):
            raise TypeError()
        self.security = security

    def execute(self):
        self.security.arm()

    def undo(self):
        self.security.disarm()


class SecurityDisarmCommand(AbsCommand):
    def __init__(self, security):
        if not isinstance(security, Security):
            raise TypeError()
        self.security = security

    def execute(self):
        self.security.disarm()

    def undo(self):
        self.security.arm()


class Actions(object):
    def __init__(self, activate, deactivate):
        self.activate = activate
        self.deactivate = deactivate


class MenuAction(object):
    def __init__(self):
        self.undo_commands = LifoQueue()
        self.commands = defaultdict(Actions)

    def set_command(self, name, activate, deactivate):
        self.commands[name] = Actions(activate, deactivate)

    def activate(self, item):
        action = self.commands[item].activate
        action.execute()
        self.undo_commands.put(action)

    def deactivate(self, item):
        action = self.commands[item].deactivate
        action.execute()
        self.undo_commands.put(action)

    def undo(self):
        if not self.undo_commands.empty():
            self.undo_commands.get().undo()
