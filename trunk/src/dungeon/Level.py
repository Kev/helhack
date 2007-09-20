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
        size = (random.randrange(8,30),random.randrange(8,30))
        x = []
        for i in range(0,size[1]):
            x.append(None)
        tiles = []
        for i in range(0,size[0]):
            tiles.append(x)
        for i in range(0,size[0]):
            logging.debug("Setting "+str(i)+",0")
            tiles[i][0] = Wall()
            logging.debug("Setting "+str(i) + ","+str(size[1] - 1))
            tiles[i][size[1] - 1] = Wall()
        for i in range(0,size[1]):
            logging.debug("Setting 0,"+str(i))
            tiles[0][i] = Wall()
            logging.debug("Setting "+str(size[1] - 1) + ","+str(i))
            tiles[size[0] - 1][i] = Wall()

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