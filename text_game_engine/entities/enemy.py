from entity import Entity

class Enemy(Entity):
    def __init__(self, name, world_map):
        super(Enemy, self).__init__(name, world_map)
