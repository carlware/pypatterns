from factory.autos.abs_auto import AutoAbs


class JeepSahara(AutoAbs):
    def start(self):
        print('Jeep Saraha running ruggedly.')

    def stop(self):
        print('Jeep Saraha shutting down.')
