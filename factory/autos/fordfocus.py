from factory.autos.abs_auto import AutoAbs


class FordFocus(AutoAbs):
    def start(self):
        print('Cool Ford Focus running smoothly.')

    def stop(self):
        print('Ford Focus shutting down.')
