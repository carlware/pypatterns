import six
import abc


class Pizza(object):

    def __init__(self):
        self.crust = ''
        self.sauce = ''
        self.meat = ''
        self.veggies = ''
        self.topping = ''

    def display(self):
        print('Handmade Pizza:')
        print('\t{:>10}: {}'.format('Crust', self.crust))
        print('\t{:>10}: {}'.format('Sauce', self.sauce))
        print('\t{:>10}: {}'.format('Meat', self.meat))
        print('\t{:>10}: {}'.format('Vegies', self.veggies))
        print('\t{:>10}: {}'.format('Topping', self.topping))


class BuilderAbs(six.with_metaclass(abc.ABCMeta)):

    def __init__(self):
        self._pizza = Pizza()

    def get_pizza(self):
        return self._pizza

    def new_pizza(self):
        self._pizza = Pizza()

    @abc.abstractmethod
    def make_crust(self):
        pass

    @abc.abstractmethod
    def add_sauce(self):
        pass

    @abc.abstractmethod
    def add_meat(self):
        pass

    @abc.abstractmethod
    def add_veggies(self):
        pass

    @abc.abstractmethod
    def add_cheese(self):
        pass


class MyPizza(BuilderAbs):
    """My favorite pizza"""

    def make_crust(self):
        self._pizza.crust = 'Whole wheat'

    def add_sauce(self):
        self._pizza.sauce = 'Tomato'

    def add_meat(self):
        self._pizza.meat = 'Sausage and Peperoni'

    def add_veggies(self):
        self._pizza.veggies = 'Tomatoes and olives'

    def add_cheese(self):
        self._pizza.topping = 'Mozarella'


class PizzaMaker(object):

    def __init__(self, builder):
        self._builder = builder

    def make_pizza(self):
        self._builder.new_pizza()
        self._builder.make_crust()
        self._builder.add_sauce()
        self._builder.add_meat()
        self._builder.add_veggies()
        self._builder.add_cheese()

    def get_pizza(self):
        return self._builder.get_pizza()
