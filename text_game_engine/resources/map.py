class Map(object):

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.world_map = [[0000 for i in range(self.x)] for j in range(self.y)]

    def update(self, entities):
        self.world_map = [[0000 for i in range(self.x)] for j in range(self.y)]
        for entity in entities:
            self.world_map[entity.pos_y][entity.pos_x] = entity.mark
