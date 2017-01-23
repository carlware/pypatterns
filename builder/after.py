import six
import abc


class Computer(object):

    def __init__(self):
        self.case = ''
        self.mainboard = ''
        self.cpu = ''
        self.memory = ''
        self.hard_drive = ''
        self.video_card = ''

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))


class BuilderAbs(six.with_metaclass(abc.ABCMeta)):

    def __init__(self):
        self._computer = Computer()

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass

    @abc.abstractmethod
    def install_hard_drive(self):
        pass

    @abc.abstractmethod
    def install_video_card(self):
        pass


class MyComputerBuilder(BuilderAbs):
    def get_case(self):
        self._computer.case = 'Coolermaster N300'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7-4770'
        self._computer.memory = 'Corsair Vengeance 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate 2TB'

    def install_video_card(self):
        self._computer.video_card = 'GeForce GTX 1070'


class BudgetBoxBuilder(BuilderAbs):
    def get_case(self):
        self._computer.case = 'IN WIN BP655'

    def build_mainboard(self):
        self._computer.mainboard = 'ASRock AM1H-ITX'
        self._computer.cpu = 'AMD Athlon 5150'
        self._computer.memory = 'Kingston ValueRAM 4GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'WD Blue 1TB'

    def install_video_card(self):
        self._computer.video_card = 'On board'


class Director(object):

    def __init__(self, builder):
        self._builder = builder  # type: BuilderAbs

    def build_computer(self):
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def get_computer(self):
        return self._builder.get_computer()
