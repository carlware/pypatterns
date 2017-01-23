from factory.autos.abs_auto import AutoAbs


class ChevyVolt(AutoAbs):
    def start(self):
        print('Chevrolet Volt running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')
