#!/usr/bin/env python
from entities import *
from resources import *

from datetime import datetime
from datetime import timedelta
from time import sleep

class Game(object):

    running=False # flag for the state machine
    next_frame=datetime.now()

    def __init__(self, width, height, num_heroes, num_enemies, tick_seconds):
        '''
        Initializes the game by creating the world - an X,Y matrix - and 
        the world's entities - a player and enemy.
        '''
        self.tick_seconds = tick_seconds
        self.world_map = map.Map(width, height)
        self.entities = []
        for i in range(num_heroes):
            self.entities.append(player.Player("H"+str(i),self.world_map))
        for i in range(num_enemies):
            self.entities.append(enemy.Enemy("E"+str(i),self.world_map))

    def start(self):
        '''
        Starts the world loop by setting the `running` flag to True
        '''
        self.running=True

    def update(self):
        '''
        The main game loop. Runs simple decision logic for each entites and
        moves them accordingly. Checks for collision etc.
        '''
        if datetime.now() < self.next_frame:
            td = self.next_frame - datetime.now()
            sleep(td.total_seconds())
        else:
            for entity in self.entities:
                entity.update()
            self.world_map.update(self.entities)
            self.next_frame = datetime.now() + \
                timedelta(seconds=self.tick_seconds)

    def render(self):
        '''
        Displays the world. For first iteration this means printing the matrix.
        '''
        for row in self.world_map.world_map:
            print " ".join([str(i).rjust(4) for i in row])
        print ""

    def quit(self):
        '''
        Breaks the game loop??? Releases the resources'''
        pass

def main():
    WIDTH=25
    HEIGHT=10
    TICK=.1
    NUM_HEROES=10
    NUM_ENEMIES=20

    game=Game(WIDTH,HEIGHT,NUM_HEROES,NUM_ENEMIES,TICK)
    game.start()
    while game.running:
        game.update()
        game.render()
    game.quit()

if __name__ == "__main__":
    main()
