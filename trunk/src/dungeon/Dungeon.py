# Dungeon.py - Dungeons.
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

from dungeon import Level

class Dungeon:
    """ Class representing a dungeon.
    """
    def __init__(self):
        """ Default constructor - do not use this (consider private)
        """
        self.levels = []

    def buildRandom():
        """Static constructor for a random dungeon
        """
        dungeon = Dungeon()
        dungeon.addLevel(Level.Level.buildRandom())
        return dungeon
    
    def addLevel(self, level):
        self.levels.append(level)
        
    def getLevel(self, level):
        return self.levels[levels]
    
    buildRandom = staticmethod(buildRandom)