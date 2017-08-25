import abc
import six


@six.with_metaclass(abc.ABCMeta)
class MyABC(object):
	"""Abstract Base Class Definition"""

	@abc.abstractmethod
	def do_something(self, value):
		"""Required method"""

	@abc.abstractproperty
	def some_property(self):
		"""Required property"""


class MyClass(MyABC):
	"""Implementation of MyABC"""

	def __init__(self, value=None):
		self._myprop = value

	def do_something(self, value):
		"""Implementation of abstract method"""
		self._myprop *= 2 + value

	@property
	def some_property(self):
		"""Implementation of abstract property"""
		return self._myprop