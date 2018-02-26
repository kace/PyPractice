import abc
class Entity(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self, name):
        self.pos_x = 0
        self.pos_y = 0
        self.name = name
