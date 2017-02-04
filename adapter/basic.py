import abc
import six
import logging


class AbsLogger(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def info(self, st):
        """required"""

    @abc.abstractmethod
    def debug(self, st):
        """required"""

    @abc.abstractmethod
    def err(self, st):
        """required"""


class BasicLogger(AbsLogger):
    def info(self, st):
        print(st)

    def debug(self, st):
        print(st)

    def err(self, st):
        print(st)


class BetterLogging(AbsLogger):

    def __init__(self):
        self._logger = logging

    def info(self, st):
        self._logger.info(st)

    def debug(self, st):
        self._logger.debug(st)

    def err(self, st):
        self._logger.error(st)


class Logging(object):

    def __init__(self, logger):
        self._logger = logger  # type: AbsLogger

    def info(self, st):
        self._logger.info(st)

    def debug(self, st):
        self._logger.debug(st)

    def error(self, st):
        self._logger.err(st)
