import six
import abc
import state as State


class User(object):
    pass


class Process(object):
    pass


class File(object):
    pass


class Server(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def __init__(self):
        """required"""
        self.name = ''

    def __repr__(self):
        return self.name

    @abc.abstractmethod
    def boot(self):
        """required"""

    @abc.abstractmethod
    def kill(self, restart=True):
        """required"""


class FileServer(Server):

    def __init__(self):
        """actions required for initializing the file server"""
        super(FileServer, self).__init__()
        self.name = 'FileServer'
        self.state = State.NEW

    def boot(self):
        """actions required for booting the file server"""
        print('booting the {}'.format(self))
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions required for killing the file server"""
        print('Killing {}'.format(self))
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_file(self, user, name, permissions):
        """check validity of permissions, user rights, etc."""
        print("trying to create the file '{}' for user '{}' with permissions{}".format(name, user, permissions))


class ProcessServer(Server):

    def __init__(self):
        """actions required for initializing the process server"""
        super(ProcessServer, self).__init__()
        self.name = 'ProcessServer'
        self.state = State.NEW

    def boot(self):
        """actions required for booting the process server"""
        print('booting the {}'.format(self))
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions required for killing the process server"""
        print('Killing {}'.format(self))
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_process(self, user, name):
        """check user rights, generate PID, etc."""
        print("trying to create the process '{}' for user'{}'".format(name, user))


class WindowServer(object):
    pass


class NetworkServer(object):
    pass
