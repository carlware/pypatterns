import six
import abc


class Subject(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def weather(self):
        pass

    @classmethod
    def create(cls):
        return ForeCastProxy(Forecast())


class Forecast(Subject):
    """Business object"""
    def weather(self):
        print('Weather is 26')


class ForeCastProxy(Subject):
    def __init__(self, forecast):
        self.forecast = forecast

    def weather(self):
        print('adding extras before')
        self.forecast.weather()
        print('adding extras after')
