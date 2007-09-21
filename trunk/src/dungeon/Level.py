# Level.py - A single level of the dungeon.
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

import logging
from item.Wall import Wall
import random

class Level:
    """ Represents a single level of the dungeon.
    """
    
    def __init__(self, tiles):
        """ Default constructor: do not use, consider private.
        """
        self.tiles = tiles
    
    def buildRandom():
        """ Build a random level
        """
        size = (random.randrange(8,20),random.randrange(8,50))
        tiles = []
        wall = Wall()
        for i in range(0,size[0]):
            x = []
            for i in range(0,size[1]):
                x.append(wall)
            tiles.append(x)
        
        for roomIndex in range(0, max(3, random.randrange(size[0]*size[1]/50))):
            logging.info("Trying to build room %d in level" % roomIndex)
            #it's possible to run away in an infinite loop,
            #bail out if it looks like we will.
            runAwayLimit = 50
            while runAwayLimit > 0:
                runAwayLimit -= 1
                logging.debug("Attempting to add a room, %d attempts left", runAwayLimit)
                roomCorner = (random.randrange(size[0] - 5), random.randrange(size[0] - 5))
                roomSize = (max(4, random.randrange(size[0] / 3)), max(4, random.randrange(size[1] / 3)))
                valid = True
                for y in range(roomCorner[0], roomCorner[0] + roomSize[0]):
                    if y >= size[0]:
                        valid = False
                        break
                    for x in range(roomCorner[1], roomCorner[1] + roomSize[1]):
                        if x >= size[1]:
                            valid = False
                            break
                        if tiles[y][x] != wall:
                            logging.debug("Trying to put room sized %d*%d, corner (%d,%d) failed because non-wall at (%d,%d)" %
                                (roomSize[0], roomSize[1], roomCorner[0], roomCorner[1], y, x))
                            valid = False
                if not valid:
                    logging.info("Failed creation of room, see if we should try again.")
                    continue
                for y in range(roomCorner[0], roomCorner[0] + roomSize[0]):
                    for x in range(roomCorner[1], roomCorner[1] + roomSize[1]):
                        logging.debug("Tunnelling out tile (%d,%d)" % (y,x))
                        tiles[y][x] = None
                logging.info("Room created.")
                runAwayLimit = 0
        
        level = Level(tiles)
        level.size = size
        return level
    
    def getSize(self):
        """ Returns the size of the level
        """
        return self.size
    
    def getTiles(self):
        """ Returns the tiles making up the level
        """
        return self.tiles
        
    
    buildRandom = staticmethod(buildRandom)