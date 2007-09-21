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
from item.ItemFactory import ItemFactory
from creature.CreatureFactory import CreatureFactory
import random

class Level:
    """ Represents a single level of the dungeon.
    """
    
    def __init__(self, tiles, creatureTiles):
        """ Default constructor: do not use, consider private.
        """
        self.tiles = tiles
        self.creatureTiles = creatureTiles
    
    def buildRandom(skillLevel):
        """ Build a random Level, with creatures and items appropriate to the skillLevel.
        """
        size = (random.randrange(20,40),random.randrange(40,80))
        tiles = []
        creatureTiles = []
        wall = Wall()
        for i in range(0,size[0]):
            x = []
            creatureX = []
            for i in range(0,size[1]):
                x.append(wall)
                creatureX.append(None)
            tiles.append(x)
            creatureTiles.append(creatureX)
        
        Level.carveRooms(tiles, size)
        Level.placeItems(tiles, size, skillLevel)
        Level.placeCreatures(tiles, creatureTiles, size, skillLevel)
        level = Level(tiles, creatureTiles)
        level.size = size
        return level

    def placeItems(tiles, size, skillLevel):
        """ Takes the provided tile grid, and adds items (of an appropriate level) to it.
        """
        for itemIndex in range(0, max(size[0]*size[1]/100, random.randrange(size[0]*size[1]/30))):
            logging.info("Trying to place item %d in level (skill level %d)" % (itemIndex, skillLevel))
            runAwayLimit = 50
            item = ItemFactory.getItem(skillLevel)
            while runAwayLimit > 0:
                runAwayLimit -= 1
                position = (random.randrange(size[0]), random.randrange(size[1]))
                if tiles[position[0]][position[1]] == None:
                    tiles[position[0]][position[1]] = item
                    runAwayLimit = 0
    
    def placeCreatures(tiles, creatureTiles, size, skillLevel):
        """ Takes the provided tile grid, and adds creatures (of an appropriate level) to it.
        """
        for creatureIndex in range(0, max(size[0]*size[1]/100, random.randrange(size[0]*size[1]/30))):
            logging.info("Trying to place item %d in level (skill level %d)" % (creatureIndex, skillLevel))
            runAwayLimit = 50
            creature = CreatureFactory.getCreature(skillLevel)
            while runAwayLimit > 0:
                runAwayLimit -= 1
                position = (random.randrange(size[0]), random.randrange(size[1]))
                if creatureTiles[position[0]][position[1]] != None:
                    continue
                if tiles[position[0]][position[1]] != None:
                    if tiles[position[0]][position[1]].isBlocking():
                        continue
                    
                creatureTiles[position[0]][position[1]] = creature
                runAwayLimit = 0
    
    def carveRooms(tiles, size):
        """ Takes the provided tile grid, and carves rooms out of it.
        """
        for roomIndex in range(0, max(3, random.randrange(size[0]*size[1]/100))):
            logging.info("Trying to build room %d in level" % roomIndex)
            #it's possible to run away in an infinite loop,
            #bail out if it looks like we will.
            runAwayLimit = 50
            while runAwayLimit > 0:
                runAwayLimit -= 1
                logging.debug("Attempting to add a room, %d attempts left", runAwayLimit)
                roomCorner = (random.randrange(size[0] - 5), random.randrange(size[1] - 5))
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
                        if not isinstance(tiles[y][x], Wall):
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
    
    def getSize(self):
        """ Returns the size of the level
        """
        return self.size
    
    def getTiles(self):
        """ Returns the tiles making up the level
        """
        return self.tiles
    
    def getCreatures(self):
        """ Returns the creatures on the level
        """
        return self.creatureTiles
    
    buildRandom = staticmethod(buildRandom)
    carveRooms = staticmethod(carveRooms)
    placeItems = staticmethod(placeItems)
    placeCreatures = staticmethod(placeCreatures)