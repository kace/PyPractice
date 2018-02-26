#!/usr/bin/env python

class Game(object):

    running=False # flag for the state machine

    def __init__(self, width, height, num_heroes, num_enemies):
        '''
        Initializes the game by creating the world - an X,Y matrix - and 
        the world's entities - a player and enemy.
        '''
        pass

    def start(self):
        '''
        Starts the world loop by setting the `running` flag to True
        '''
        running=True

    def process(self):
        '''
        The main game loop. Runs simple decision logic for each entites and
        moves them accordingly. Checks for collision etc.
        '''
        pass

    def render(self):
        '''
        Displays the world. For first iteration this means printing the matrix.
        '''
        pass

    def quit(self):
        '''
        Breaks the game loop??? Releases the resources'''
        pass

def main():
    pass

if __name__ == "__main__":
    game=Game()
    game.init()
    game.start()
    while game.running():
        # FRAME
        # PROCESS
        # RENDER
    game.quit()
