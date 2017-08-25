import abc
import six


class Order(object):
    def __init__(self):
        pass


class Shipper(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def calculate(self, order):
        """abstract method"""


class UPS(Shipper):

    def calculate(self, order):
        return 4.00


class Fedex(Shipper):

    def calculate(self, order):
        return 3.00


class Postal(Shipper):

    def calculate(self, order):
        return 5.00


class ShippingCost(object):

    def __init__(self, shipper):
        self._shipper = shipper

    def cost(self, order):
        return self._shipper.calculate(order)
