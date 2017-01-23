import six
import abc

class Expression(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def get_value(self):
        """required"""


class Constant(Expression):

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def __repr__(self):
        return '{}'.format(self._value)


class BinaryExpression(six.with_metaclass(abc.ABCMeta)):

    def __init__(self, left, right):
        self._left = left  # type: Expression
        self._right = right  # type: Expression

    @abc.abstractmethod
    def get_value(self):
        """required"""

    def __repr__(self):
        return '({} ? {})'.format(self._left, self._right)


class Adder(BinaryExpression):

    def get_value(self):
        return self._left.get_value() + self._right.get_value()

    def __repr__(self):
        return '({} + {})'.format(self._left, self._right)


class Subtracter(BinaryExpression):

    def get_value(self):
        return self._left.get_value() - self._right.get_value()

    def __repr__(self):
        return '({} - {})'.format(self._left, self._right)


class Divider(BinaryExpression):

    def get_value(self):
        return self._left.get_value() / self._right.get_value()

    def __repr__(self):
        return '({} / {})'.format(self._left, self._right)


class Multiplier(BinaryExpression):

    def get_value(self):
        return self._left.get_value() * self._right.get_value()

    def __repr__(self):
        return '({} * {})'.format(self._left, self._right)


class Stack(list):

    def is_empty(self):
        return not self

    def push(self, item):
        self.append(item)

    def pop(self, index=0):
        return self.pop(index)


class ParseExpression(object):
    ope = list('*-+/')
    strategies = {
        '+': Adder,
        '-': Subtracter,
        '*': Multiplier,
        '/': Divider,
    }

    def __init__(self, exp):
        self._exp = exp  # type: str

    def eval(self):
        items = self._exp.split(' ')
        const = list()
        binaries = list()

        e = None
        for item in items:
            if item == ')':
                right = const.pop()
                left = const.pop()
                e = self.strategies[binaries.pop()](left, right)
                const.append(e)
            elif item in self.ope:
                binaries.append(item)
            elif item == '(':
                continue
            else:
                const.append(Constant(float(item)))

        if len(binaries) > 0:
            right = const.pop()
            left = const.pop()
            e = self.strategies[binaries.pop()](left, right)

        return e

    @classmethod
    def builder(cls, exp):
        return cls(exp).eval()
