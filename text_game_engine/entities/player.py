from entity import Entity
class Player(Entity):
    
    def __init__(self, name, world_map):
        super(Player, self).__init__(name, world_map)
