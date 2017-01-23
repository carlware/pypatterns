import abc
import six


# domain
class Observer(six.with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def update(self, value):
        """required"""

    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Subject(six.with_metaclass(abc.ABCMeta)):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, Observer):
            raise TypeError('observer is not instance of Observer')
        self._observers |= {observer}

    def notify(self, value=None):
        for obs in self._observers:
            obs.update(value)

    def detach(self, observer):
        self._observers -= {observer}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()


# concrete implementation
class CurrentKPIs(Observer):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def get_state(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

    def update(self, value=None):
        self.get_state()
        self.display()

    def display(self):
        print('Current open tickets: {}'.format(self.open_tickets))
        print('New tickets in last hour: {}'.format(self.closed_tickets))
        print('Tickets closed in last hour: {}'.format(self.new_tickets))
        print('*****\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)


class ForecastKPIs(Observer):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def get_state(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

    def update(self, value=None):
        self.get_state()
        self.display()

    def display(self):
        print('Forecast open tickets: {}'.format(self.open_tickets))
        print('New tickets expected in next hour: {}'.format(self.closed_tickets))
        print('Tickets expected to be closed in next hour: {}'.format(self.new_tickets))
        print('*****\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)


class KPIs(Subject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()
