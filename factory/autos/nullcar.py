from factory.autos.abs_auto import AutoAbs


class NullCar(AutoAbs):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s".' % self._carname)

    def stop(self):
        pass
