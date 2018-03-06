from entity import Entity

class Enemy(Entity):
    def __init__(self, name, world_map):
        super(Enemy, self).__init__(name, world_map)
        self.pos_x = self.world_map.x
        self.pos_y = self.world_map.y
