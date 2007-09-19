# Item.py - Base class for all objects ingame, including scenery, 
#           potions, whatever.
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

class Item:
	""" Base class for all ingame objects, including creatures and scenery
	"""
	
	def __init__(self):
		self.blocking = False
		self.carryable = False
		self.glyph = "@"
		self.colour = curses.COLOR_WHITE
	
	def isBlocking(self):
		""" Does this item prevent movement on a map?
		"""
		return self.blocking
	
	def isCarryable(self):
		""" Can this item be carried in a backpack?
		"""
		return self.carryable

	def getGlyph(self):	
		""" The character used to render this in curses.
		"""
		return self.glyph
	
	def getColour(self):
		""" The colour used to render this tile in curses.
		"""
		return self.colour
		