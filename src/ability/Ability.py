# Ability.py - Base class for all creature abilities, such as
#              attack, cast spell, etc
# Copyright Stefan Brus 2007.
#
# This file is part of HelHack.
#
# HelHack is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# HelHack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ability.Effect import Effect

class Ability:
    """ Base class for all creature abilities such as attack, cast spell, etc
    """

    def __init__(self):
        self.cost = 0
        self.name = ""
        self.power = 0
        self.effects = []

    def getCost(self):
        """ Returns the ability cost
        """
        return self.cost

    def getName(self):
        """ Returns the ability name
        """
        return self.name

    def getPower(self):
        """ Returns the ability power
        """
        return self.power

    def getEffects(self):
        """ Returns a list of ability effects
        """
        return self.effects
