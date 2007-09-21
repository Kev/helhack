# Creature.py - Base class for all living creatures in the game.
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

from item.Item import Item
import curses

class Creature(Item):
    """ This class provides the basis of all creatures in the game.
    """
    
    def __init__(self):
        self.level = 1 # The creature's overall level
        self.inventory = [] # items the creature is carrying
        self.classes = []
        self.races = []
        self.glyph = "+"
        self.color = curses.COLOR_BLUE
        self.currentClass = None
    
    def addRace(self, newRace):
        """ Add a new race
        """
        self.races.append(newRace)
        
    def addClass(self, newClass):
        """ Add a new class
        """
        self.classes.append(newClass)
        if self.currentClass == None:
            self.currentClass = newClass
            
    def levelUp(self, increment = 1):
        self.currentClass.levelUp(increment)