# CursesController.py - Main class for a curses game.
# Copyright Kevin Smith 2007.
#
# This file is part of HelHack.
#
# HelHack is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import curses
import logging
from dungeon.Dungeon import Dungeon
from item.Wall import Wall
import random 

class CursesController:
    def __init__(self):
        """ Set up the terminal.
        """
        random.seed()
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        #FIXME we need to check for colour first
        curses.start_color()
        self.screen.clear()
        self.screen.refresh()
        logging.debug("Rarr, controller created")
        self.dungeon = Dungeon.buildRandom()
        self.currentLevel = 0
        self.mapCentre = (self.dungeon.getLevel(self.currentLevel).getSize()[0]/2,
                            self.dungeon.getLevel(self.currentLevel).getSize()[1]/2)
        self.count = 0 # debugging only
        
    
    def __del__(self):
        """ Clear up the terminal before dying.
        """
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        logging.debug("Arr, fate be a harsh mistress; controller down.")
    
    def render(self):
        logging.debug("Painting")
        self.screen.clear()
        logging.debug("Level is sized %s by %s" % self.dungeon.getLevel(self.currentLevel).getSize())
        mapSize = self.dungeon.getLevel(self.currentLevel).getSize()
        screenSize = self.screen.getmaxyx()
        wall = Wall()
        for screenY in range(0, screenSize[0]-1):
            mapY = self.mapCentre[0] - screenSize[0] /2 + screenY
            inYRange = True
            if mapY < 0 or mapY >= mapSize[0]:
                #logging.debug("Tile (%d,x) is out of map range " % (mapY))
                inYRange = False
                
            for screenX in range(0, screenSize[1]):
                inRange = inYRange
                mapX = self.mapCentre[1] - screenSize[1] /2 + screenX
                if mapX < 0 or mapX >= mapSize[1]: 
                    #logging.debug("Tile (%d,%d) is out of map range " % (mapY, mapX))
                    inRange = False
                #logging.debug("Tile (%d,%d) %d" % (mapY, mapX, inRange))
                if inRange:
                    #logging.debug("Getting tile (%d, %d)" % (mapY, mapX))
                    tile = self.dungeon.getLevel(self.currentLevel).getTiles()[mapY][mapX]
                else:
                    tile = wall
                if tile == None:
                    #logging.debug("Tile (%d,%d) is empty." % (mapY,mapX))
                    None
                else:
                    #logging.debug("Tile (%d,%d) at (%d,%d) is '%s'." % (mapY,mapX,screenY,screenX,tile.getGlyph()))
                    self.screen.addstr(screenY,screenX, tile.getGlyph())
                                
        self.screen.refresh()
                
        
    def turn(self):
        """ Take one turn of the game.
        """
        logging.debug("Taking a turn")
        
        self.render()
        self.count += 1
        self.screen.getkey()
        return False