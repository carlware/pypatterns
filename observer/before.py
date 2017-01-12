from collections import namedtuple
from itertools import starmap

data = (('new', 10), ('open', 20), ('closed',30))
nt = namedtuple('KPI', 'name value')
KPI_Data = starmap(nt, data)

def run():
    for kpi in KPI_Data:
        if kpi.name == 'open':
            print('Current open tickets: %s' % kpi.value)
        elif kpi.name == 'new':
            print('New tickets in last hour: %s' % kpi.value)
        elif kpi.name == 'closed':
            print('Tickets closed in last hour: %s' % kpi.value)
