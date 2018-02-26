import abc
class Entity(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self, name, world_map):
        self.pos_x = 0
        self.pos_y = 0
        self.mark = name
        self.world_map = world_map

    def _move(self,(x,y)):
        self.pos_x+=x
        self.pos_y+=y
        if self.pos_x < 0:
            self.pos_x = 0
        elif self.pos_x >= self.world_map.x:
            self.pos_x = self.world_map.x-1
        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y >= self.world_map.y:
            self.pos_y = self.world_map.y-1

    def move_up(self):
        self._move((0,-1))

    def move_left(self):
        self._move((-1,0))

    def move_down(self):
        self._move((0,1))

    def move_right(self):
        self._move((1,0))

    def process(self):
        # written for random movement
        movement = [self.move_up, self.move_left, self.move_down,
                self.move_right]
        from random import randint
        movement[randint(0,len(movement)-1)]()
        print self.position

    @property
    def position(self):
        return (self.pos_x, self.pos_y)
