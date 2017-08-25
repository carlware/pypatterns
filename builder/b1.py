class Computer(object):

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))


class CustomComputer(object):

    def __init__(self):
        self._computer = None

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = 'Coolermaster N300'
        computer.mainboard = 'MSI 970'
        computer.cpu = 'Intel Core i7-4770'
        computer.memory = 'Corsair Vengeance 16GB'
        computer.hard_drive = 'Seagate 2TB'
        computer.video_card = 'GeForce GTX 1070'
