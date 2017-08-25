

class Tree(object):

    def __init__(self, t_type):
        self._type = t_type

    def render(self, age, x, y):
        """
        age,x,y values have to be stored somewhere else
        """
        print('render a tree of type {} and age {} at ({},{})'.format(self._type, age, x, y))


class TreeSimpleFactory(object):
    _trees = dict()

    @classmethod
    def instance(cls, tree_type):
        if tree_type not in cls._trees:
            tree = Tree(tree_type)
            cls._trees[tree_type] = tree
        return cls._trees[tree_type]
