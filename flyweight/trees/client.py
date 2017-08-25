import random
import tree_type
from .tree import TreeSimpleFactory


class TreeClient(object):

    def __init__(self, age_min, age_max, min_point, max_point):
        self.tree_cnt = 0
        self.age_min = age_min
        self.age_max = age_max
        self.min_point = min_point
        self.max_point = max_point
        self.rnd = random.Random()

    def create_tree(self, t_type, n_trees):
        for _ in range(n_trees):
            t1 = TreeSimpleFactory.instance(t_type)
            t1.render(self.rnd.randint(self.age_min, self.age_max),
                      self.rnd.randint(self.min_point, self.max_point),
                      self.rnd.randint(self.min_point, self.max_point))
            self.tree_cnt += 1

    def run(self):
        self.create_tree(tree_type.APPLE_TREE, 10)
        self.create_tree(tree_type.CHERRY_TREE, 3)
        self.create_tree(tree_type.PEACH_TREE, 5)

        print('trees rendered: {}'.format(self.tree_cnt))
        print('trees actually created: {}'.format(len(TreeSimpleFactory._trees)))
