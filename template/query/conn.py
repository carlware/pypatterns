

class Connection(object):

    def close(self):
        pass

    def open(self):
        pass

    @staticmethod
    def execute(raw_query):
        # in fact this is an anti-pattern (use strategy)
        if 'PEOPLE' in raw_query:
            return ['John', 'Smith', 'Anderson']
        elif 'COMPANY' in raw_query:
            return ['IBM', 'DELL', 'HP', 'Alphabet']
        else:
            return []
