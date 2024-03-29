# CreatureClass.py - Base class for all classes of creature in game.
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

class CreatureClass:
    """ The base class for all different skill classes.
    """
    def __init__(self):
        self.name = "Unknown class"
        self.level = 1

    def getName(self):
        return self.name
        
    def levelUp(self, increment = 1):
        for i in range(0,increment):
            self.level += 1